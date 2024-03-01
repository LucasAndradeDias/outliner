import re

from pathlib import Path

from .modules.trace import Trace
from .modules.display import Display

from .views import ModuleObject, RunningObject


class Outliner:
    def __init__(self, file_path, object_name: str, display_type: str):
        self.file = file_path
        self.obj_name = object_name
        self.display_type = display_type
        self.callable_object_parttern = re.compile(
            r"\w+\((?:'\w+')?(?:\.\w+\('(?:\w+)'\))?\)"
        )
        self._check_file()

    def run(self):
        """
        This method trace an object and prints out a tree with found data
        """

        if not re.match(self.callable_object_parttern, self.obj_name):
            raise ValueError("Not valid callable syntax")

        module_obj = ModuleObject(Path(self.file))
        running_obj = RunningObject(module_obj, self.obj_name)

        trace = Trace()
        trace.trace_obj(running_obj)

        display_class = Display(trace.detailed_data, trace.functions_flow)

        running_display = getattr(display_class, self.display_type)
        running_display()

    def _check_file(self):
        if not Path(self.file).is_file():
            raise Exception(f"Not a valid file\nPath:'{self.file}'")
        if not ".py" in self.file:
            raise Exception("Not a python file")
