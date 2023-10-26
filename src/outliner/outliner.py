from pathlib import Path
from .modules.trace import Trace
from .modules.display import Display


class Outliner:
    def __init__(self, file_path, object_name, display_type):
        self.file = file_path
        self.obj_name = object_name
        self.display_type = display_type

    def run(self):
        """
        This method trace an object and prints out a tree with found data
        """
        self._check_file()

        trace = Trace()

        trace.run_file(Path(self.file), self.obj_name)
        display_class = Display(trace.detailed_data, trace.functions_flow)

        running_display = getattr(display_class, self.display_type)
        running_display()

    def _check_file(self):
        if not Path(self.file).is_file():
            raise ("Not a valid file")
        if not ".py" in self.file:
            raise ("Not a python file")
