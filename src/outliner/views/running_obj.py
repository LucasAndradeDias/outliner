from .module_obj import ModuleObject
from functools import partial


class Running_Obj:
    """
    Create an running object from a module obj
    """

    def __init__(self, script_obj: ModuleObject, obj_invoking: str):
        self.obj_invoking = obj_invoking
        self.script_obj = script_obj
        self.father_module = self.script_obj.module()

        self.module_obj = self.father_module[0]
        self.module_spec = self.father_module[1]

        # load the module to the global namespace
        self.module_spec.loader.exec_module(self.module_obj)

        self.running_obj = None
        self.instance()

    def _get_object_arguments(self, obj: str):
        parenthesis_1 = obj.index("(")
        parenthesis_2 = obj.index(")")
        obj_arguments = obj[parenthesis_1 + 1 : parenthesis_2].split(",")

        return obj_arguments if any(obj_arguments) else None

    def _create_obj_instance(self, namespace: any, object_: str):
        object_name = object_.split("(")[0]
        object_arguments = self._get_object_arguments(object_)
        obj_instance = getattr(namespace, object_name, None)

        if object_arguments is not None:
            obj_instance = partial(obj_instance, *object_arguments)

        return obj_instance

    def instance(self):
        """Creates an instance of the object"""
        running_obj = None
        father = self.module_obj
        objs = self.obj_invoking.split(".") or [self.obj_invoking]
        for number, _ in enumerate(objs):
            running_obj = self._create_obj_instance(father, objs[number])
            if len(objs) == number:
                break
            father = running_obj

        self.running_obj = father
        return running_obj

    def __call__(self):
        self.instance()
