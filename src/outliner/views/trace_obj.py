import ast
import importlib

from typing import Path
from pathlib import Path


class Trace_script:
    """
    Run all needed pre-sets to run the trace_object.

    Class create to transforms the script into an better handling object.
    That way, it is faster to handle with it because will use ast module to get infos about it
    """

    def __init__(
        self,
        script_path: Path,
    ):
        super(Trace_script, self).__init__()
        self.file_path = script_path
        self.object_ast = self._load_file_ast(script_path)

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

    def _load_file_ast(self, file_path) -> ast.parse:
        try:
            with open(file_path) as file:
                return ast.parse(file, file_name=file_path)
        except:
            raise ("Error opening the module file")

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
        moduleSpec = importlib.util.spec_from_file_location(module_name, module_path)
        module_obj = importlib.util.module_from_spec(moduleSpec)
        moduleSpec.loader.exec_module(module_obj)

        return module_obj


class Trace_Object(Trace_script):
    def __init__(self, script_path: Path, obj_invoking: str):
        super().__init__(script_path)
        self.obj_invoking = obj_invoking
