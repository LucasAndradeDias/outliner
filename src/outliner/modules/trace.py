import sys
import collections
import os


from pathlib import Path
from ..views import RunningObject


class ExceptionWhileTracing(Exception):
    """Exception Subclass to be raise with the first exception while tracing an object"""

    pass


class Trace:

    def __init__(self):
        self.detailed_data = collections.defaultdict(
            lambda: {
                "call": 0,
                "return": 0,
                "line": 0,
                "exception": 0,
                "file": Path(),
                "start_line": int,
            }
        )
        self.functions_flow = collections.OrderedDict()

    def _trace_function(self, frame, event, arg):

        self.detailed_data[frame.f_code.co_name][str(event)] += 1
        self.functions_flow[frame.f_code.co_name] = None
        self.detailed_data[frame.f_code.co_name]["file"] = Path(
            frame.f_code.co_filename
        )
        self.detailed_data[frame.f_code.co_name][
            "start_line"
        ] = frame.f_code.co_firstlineno

        return self._trace_function

    def _running_trace(self, obj) -> None:
        try:
            instance = obj.instance()
            sys.stdout = open(os.devnull, "w")
            sys.settrace(self._trace_function)
            instance()
            sys.settrace(None)
        except Exception as error:
            raise (f"Erro durante execução: {str(error)}")
        finally:
            sys.settrace(None)
            sys.stdout = sys.__stdout__
            return

    def trace_obj(self, running_obj: RunningObject):
        if not callable(running_obj):
            raise Exception(f"Given object '{running_obj}' is not callable.")
        self._running_trace(running_obj)

    def __str__(self):
        text = "Trace object\nrunned objects:\n    "

        for i in self.detailed_data:
            text = text + i + "\n    "

        return text

    def __repr__(self):
        text = r"Trace object\nrunned objects:\n    "

        for i in self.detailed_data:
            text = text + rf"{i} + \n    "

        return text
