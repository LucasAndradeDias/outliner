from importlib import util
from pathlib import Path


def find_module_path(name: str, root_path: Path) -> Path:
    """
    Find a module Pathlike object
        Returns Posix
    """
    found_modules = list(root_path.glob(f"**/{name}.py"))
    return found_modules[0] if any(found_modules) else None

def add_import_module_to_namespace(modules: set):
    """
    Add all local modules used in script to the global namespace
    arguments:
    @param cls: script_obj
    """
    for import_module in modules:
        module_name = import_module[0]
        module_path = import_module[1]
        module_spec = util.spec_from_file_location(module_name,str(module_path))
        module_obj = util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module_obj)        
