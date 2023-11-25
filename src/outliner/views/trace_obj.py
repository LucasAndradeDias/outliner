import ast
from typing import Path
from pathlib import Path


class Trace_object:
    """
    Class create to transforms the script into an better handling object.
    That way, it is faster to handle with it because will use ast module to get infos about it
    """

    def __init__(self, file_path: Path, object_invoke: str):
        self.file_path = file_path
        self.object_invoke = object_invoke
        self.object_ast = self._load_file_ast(file_path)

    def imported_modules(self) -> list:
        """
        A generator with all imports the object contains in its namespace
        """
        for node in ast.walk(self.object_ast):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    yield alias.name
            elif isinstance(node, ImportFrom):
                if node.module is not None:
                    yield nome.module
        return []

    def _load_file_ast(self, file_path) -> ast.parse:
        try:
            with open(file_path) as file:
                return ast.parse(file, file_name=file_path)
        except:
            raise ("Error opening the module file")

    def _check_class(self):
        ...
