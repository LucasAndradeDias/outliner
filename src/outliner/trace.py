import sys
import collections
import importlib.util


class Trace:
    def __init__(self):
        self.detailed_data = collections.defaultdict(
            lambda: {"call": 0, "return": 0, "line": 0}
        )
        self.functions_flow = collections.OrderedDict()

    def trace_function(self, frame, event, arg):
        self.detailed_data[frame.f_code.co_name][str(event)] += 1

        self.functions_flow[frame.f_code.co_name] = None

        return self.trace_function





    def run(self, module_name: str, func: str, func_params=None):
        try:
            trace_import = importlib.util.spec_from_file_location(func, module_name)
            trace_obj = importlib.util.module_from_spec(trace_import)

            trace_import.loader.exec_module(trace_obj)

            method = None

            if func_params:
                method = getattr(trace_obj, func)(*func_params)
            else:
                method = getattr(trace_obj, func)

            if not callable(method):
                raise Exception(f"given object '{func}' is not callable.")

            sys.settrace(self.trace_function)
            method()
            sys.settrace(None)

        except Exception as error:
            raise (error)
