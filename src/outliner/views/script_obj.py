import ast
import sys

from importlib import util
from pathlib import Path
from helpers.find_module import find_module_path


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
        self._imported_modules = self._find_imported_modules()
        self._add_imports()

    def _find_imported_modules(self) -> iter:
        """
        A generator with all imports the ast object contains in its namespace
        """
        for node in ast.walk(self.object_ast):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    yield alias.name
            elif isinstance(node, ast.ImportFrom):
                if node.module is not None:
                    yield node
        return []

    def _load_file_ast(self) -> ast.parse:
        with open(self.script_path, "r") as file:
            return ast.parse(file.read())

    def _add_imports(self) -> None:
        """
        Add all found imports to the running gloabal namespace
        """
        try:
            sys.path.append(find_module_path(i) for i in self._imported_modules)
        except:
            raise "Error while adding imports modules"

    def module(self):
        """
        Return a spec (https://peps.python.org/pep-0451/) object for running the module
        """
        module_name = self.script_path.stem
        moduleSpec = util.spec_from_file_location(module_name, self.script_path)
        module_obj = util.module_from_spec(moduleSpec)
        moduleSpec.loader.exec_module(module_obj)

        return module_obj
