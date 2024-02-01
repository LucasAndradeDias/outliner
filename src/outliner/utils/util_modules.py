from pathlib import Path


def find_module_path(name: str, root_path: Path) -> Path:
    """
    Find a module Pathlike object
        Returns Posix
    """
    found_modules = list(root_path.glob(f"**/{name}.py"))
    return str(found_modules[0].parent) if any(found_modules) else None
