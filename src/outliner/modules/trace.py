import sys
import collections
import importlib.util


class Trace:
    def __init__(self):
        self.detailed_data = collections.defaultdict(
            lambda: {"call": 0, "return": 0, "line": 0}
        )
        self.functions_flow = collections.OrderedDict()

    def _trace_function(self, frame, event, arg):
        self.detailed_data[frame.f_code.co_name][str(event)] += 1
        self.functions_flow[frame.f_code.co_name] = None
        return self._trace_function

    def run_file(self, module_name: str, func: str, func_params=None):
        try:
            trace_import = importlib.util.spec_from_file_location(func, module_name)
            trace_obj = importlib.util.module_from_spec(trace_import)
            trace_import.loader.exec_module(trace_obj)

            object_to_run = getattr(trace_obj, func, None)

            if not callable(object_to_run):
                raise Exception("given object '%s' is not callable." % (func))

            if func_params:
                self._running_trace(object_to_run, *func_params)
            else:
                self._running_trace(object_to_run)

        except Exception as e:
            raise Exception("Error on the execution of the module: \n %s" % (e))

    def _running_trace(self, obj, *arguments):
        if arguments:
            sys.settrace(self._trace_function)
            obj(*arguments)
            sys.settrace(None)
        else:
            sys.settrace(self._trace_function)
            obj()
            sys.settrace(None)

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
