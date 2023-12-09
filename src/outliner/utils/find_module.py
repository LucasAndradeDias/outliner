from pathlib import Path
import pathlib


def find_module_path(name: str, root_path: Path) -> Path:
    """
    Find a module Pathlike object
    """
    try:
        for i in set(root_path.glob("**/*.py")):
            if i.stem == name:
                return i
        return None
    except:
        raise "Error trying fiding modules"
