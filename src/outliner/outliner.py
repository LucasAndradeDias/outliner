import argparse
import sys

from pathlib import Path
from .trace import Trace
from .display import Display


class Outliner:
    def __init__(self, file_path, object_name, object_args=None):
        self.file = file_path
        self.obj_name = object_name
        self.obj_args = object_args

    def run(self):
        """
        This method trace an object and prints out a tree with found data
        """

        # verify file
        self._check_file()

        trace = Trace()
        trace.run(self.file, self.obj_name, self.obj_args if self.obj_args else None)
        display_class = Display(trace.detailed_data, trace.functions_flow)
        display_class.tree()

    def _check_file(self):
        if not Path(self.file).is_file():
            raise ("Not a valid file")
        if not ".py" in self.file:
            raise ("Not a python file")
