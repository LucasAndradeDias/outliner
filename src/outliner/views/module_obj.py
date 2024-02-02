import sys
import ast
import importlib

from importlib import util
from pathlib import Path
from utils.loader import CustomLoader


class ModuleObject:
    """
    Run all needed pre-sets to run the trace_object.

    Class create to transforms the script into an better handling object.
    That way, it is faster to handle with it because will use ast module to get infos about it
    """

    def __init__(
        self,
        module_path: Path,
    ):
        self.module_path = module_path
        self.module_ast = self._load_file_ast()
        self.found_submodules = self._find_imported_modules()

        sys.path.append(str(module_path.parent))

        for submodule in self.found_submodules:
            try:
                importlib.import_module(submodule)
            except ModuleNotFoundError:
                raise ModuleNotFoundError(
                    f"Could not add the submodule '{submodule}' to the namespace.\n check if the module is installed."
                )

    def _find_imported_modules(self) -> iter:
        """
        A generator with all imports the ast object contains in its namespace
        """
        for node in ast.walk(self.module_ast):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    yield alias.name
            elif isinstance(node, ast.ImportFrom):
                if node.module is not None:
                    yield node.module
        return []

    def _load_file_ast(self) -> ast.parse:
        with open(self.module_path, "r") as file:
            return ast.parse(file.read())

    def module(self):
        """
        Return a the ModuleObj and the ModuleSpec (https://peps.python.org/pep-0451/) of the module
        """
        module_name = self.module_path.stem
        module_spec = util.spec_from_file_location(
            name=module_name, location=self.module_path, loader=CustomLoader
        )

        module_obj = util.module_from_spec(module_spec)

        return module_obj, module_spec
