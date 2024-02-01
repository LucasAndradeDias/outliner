import ast

from importlib import util
from pathlib import Path
from utils.util_modules import find_module_path
from utils.loader import Loader


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

        # Set with all imported modules the module obj contains
        self.used_modules = set(())

        for module in self._imported_modules:
            mod_path = find_module_path(module, self.script_path.parent)
            if mod_path:
                self.used_modules.add((module, mod_path))

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
                    yield node.module
        return []

    def _load_file_ast(self) -> ast.parse:
        with open(self.script_path, "r") as file:
            return ast.parse(file.read())

    def module(self):
        """
        Return a ModuleSpec (https://peps.python.org/pep-0451/) object of a module
        """

        # class _NamespacePath adiciona pro namespace

        # This class is actually exposed publicly in a namespace package's __loader__
        # # attribute, so it should be available through a non-private name.
        # # https://bugs.python.org/issue35673
        # class NamespaceLoader:

        module_name = self.script_path.stem
        module_spec = util.spec_from_file_location(
            name=module_name,
            location=self.script_path,
            submodule_search_locations=["D:\projects\scripts\outliner\tests-outliner"],
        )
        module_obj = util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module_obj)

        return module_obj
