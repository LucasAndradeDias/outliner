from .script_obj import Script_Obj
from functools import partial


class Running_Obj:
    def __init__(self, script_obj: Script_Obj, obj_invoking: str):
        self.obj_invoking = obj_invoking
        self.script_obj = script_obj

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
        """Returns a instance of the object"""

        running_obj = None
        father = self.script_obj.module()
        objs = self.obj_invoking.split(".") or [self.obj_invoking]

        for number, _ in enumerate(objs):
            running_obj = self._create_obj_instance(father, objs[number])
            if len(objs) == number:
                break
            father = running_obj()

        return running_obj

    def __call__(self):
        self.instance()
