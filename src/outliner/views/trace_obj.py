import ast

from importlib import util
from pathlib import Path
from functools import partial


class Script_Obj:
    """
    Run all needed pre-sets to run the trace_object.

    Class create to transforms the script into an better handling object.
    That way, it is faster to handle with it because will use ast module to get infos about it
    """

    def __init__(
        self,
        script_path: Path,
    ):
        self.script_path = script_path
        self.object_ast = self._load_file_ast()

    def _find_imported_modules(self) -> list:
        """
        A generator with all imports the object contains in its namespace
        """
        for node in ast.walk(self.object_ast):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    yield alias.name
            elif isinstance(node, ast.ImportFrom):
                if node.module is not None:
                    yield node.module
        return []

    def _load_file_ast(self) -> ast.parse:
        with open(self.script_path, "r") as file:
            return ast.parse(file.read())

    def add_imports(self) -> None:
        """
        Add all found imports to the running gloabal namespace
        """
        ...

    def module(self):
        """
        Return a spec (https://peps.python.org/pep-0451/) object for running the module
        """
        module_name = self.script_path.stem
        moduleSpec = util.spec_from_file_location(module_name, self.script_path)
        module_obj = util.module_from_spec(moduleSpec)
        moduleSpec.loader.exec_module(module_obj)

        return module_obj


class Trace_Obj:
    def __init__(self, script_obj: Script_Obj, obj_invoking: str):
        self.obj_invoking = obj_invoking
        self.script_obj = script_obj

    def _get_object_arguments(self, obj: str):
        parenthesis_1 = obj.index("(")
        parenthesis_2 = obj.index(")")
        obj_arguments = obj[parenthesis_1 + 1 : parenthesis_2].split(",")
        return None if not any(obj_arguments) else obj_arguments

    def _create_obj_instance(self, namespace: any, object_: str):
        object_name = object_.split("(")[0]
        object_arguments = self._get_object_arguments(object_)

        obj_instance = getattr(namespace, object_name, None)

        if object_arguments:
            obj_instance = partial(obj_instance, *object_arguments)

        return obj_instance

    def create(self):
        """Returns a instance of the object"""

        running_obj = None
        father = self.script_obj.module()
        objs = self.obj_invoking.split(".") or [self.obj_invoking]

        for number, _ in enumerate(objs):
            running_obj = self._create_obj_instance(father, objs[number])

            if len(objs) == number:
                break
            father = running_obj
        return running_obj