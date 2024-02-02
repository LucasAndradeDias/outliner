import importlib
import importlib.abc
from types import ModuleType


class CustomLoader(importlib.abc.Loader):
    def __init__(self) -> None:
        super().__init__()

    def create_module(spec) -> object:
        return None

    def exec_module(module: ModuleType) -> None:
        with open(module.__spec__.origin, "rb") as f:
            code = compile(f.read(), module.__spec__.origin, "exec")
            exec(code, module.__dict__)
