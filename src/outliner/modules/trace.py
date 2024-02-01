import sys

import collections
import importlib.util

from functools import partial
from pathlib import Path
from typing import Optional


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
            sys.settrace(self._trace_function)
            obj()
        except ExceptionWhileTracing as error:
            return
        except Exception as error:
            raise error
        finally:
            sys.settrace(None)

    def run_file(
        self,
        module_path: Path,
        object_to_run: str,
    ) -> None:
        """
        Trace a file

        :param Path-like module_path: The path to the module
        :param str object_to_run: The object to be traced inside the module
        """
        module_name = module_path.stem

        moduleSpec = importlib.util.spec_from_file_location(module_name, module_path)
        module_obj = importlib.util(moduleSpec)

        moduleSpec.loader.exec_module(module_obj)

        # Check the type of the object(class method or function)
        if len(object_to_run.split(".")) >= 2:
            obj_class_instance = self._create_obj_instance(
                module_obj, object_to_run.split(".")[0]
            )()
            running_obj = self._create_obj_instance(
                obj_class_instance, object_to_run.split(".")[1]
            )
        else:
            running_obj = self._create_obj_instance(module_obj, object_to_run)

        if not callable(running_obj):
            raise Exception("given object '%s' is not callable." % (module_name))

        self._running_trace(running_obj)

    def trace_obj(self,running_obj):
        
        if not callable(running_obj):
            raise Exception("given object '%s' is not callable." % (module_name))
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
