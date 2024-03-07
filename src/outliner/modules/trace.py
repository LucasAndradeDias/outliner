import sys
import collections

from ..views import RunningObject


class ExceptionWhileTracing(Exception):
    """Exception Subclass to be raise with the first exception while tracing an object"""

    pass




class Trace:

    def __init__(self):
        self.detailed_data = collections.defaultdict(
            lambda: {"call": 0, "return": 0, "line": 0, "exception": 0}
        )
        self.functions_flow = collections.OrderedDict()

    def _trace_function(self, frame, event, arg):
        self.detailed_data[frame.f_code.co_name][str(event)] += 1
        self.functions_flow[frame.f_code.co_name] = None

        if str(event) == "exception":
            raise ExceptionWhileTracing()

        return self._trace_function

    def _running_trace(self, obj) -> None:
        try:
            instance = obj.instance()
            sys.settrace(self._trace_function)
            instance()
        except ExceptionWhileTracing as error:
            return
        except Exception:
            raise Exception("Erro durante execução")
        finally:
            sys.settrace(None)

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
