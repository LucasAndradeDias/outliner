import unittest
import collections
import sys

from pathlib import Path
from src.outliner import Trace
from unittest.mock import patch
from io import StringIO

from src.outliner.views import ModuleObject, RunningObject


class TestTrace(unittest.TestCase):
    def setUp(self):
        self.base_path = Path(__file__).resolve()
        self.mock_path = str(self.base_path.parent / "data")
        self.parser = Trace()

    def tearDown(self):
        self.parser.detailed_data = collections.defaultdict(
            lambda: {"call": 0, "return": 0, "line": 0}
        )
        self.parser.functions_flow = collections.OrderedDict()

    def test_trace_obj_positive_input(self):
        """
        Given a valid running obj
        When trace.trace_obj is called with this parameter
        Then the running_obj should be executed and the class property updated
        """
        module_obj = ModuleObject(Path(self.mock_path + "/module_testing_1.py"))
        module_running_obj = RunningObject(module_obj, "test()")
        self.parser.trace_obj(module_running_obj)
        expected_trace = r"Trace object\nrunned objects:\n    __init__ + \n    func1 + \n    func2 + \n    "
        self.assertEqual(expected_trace, repr(self.parser))

    def test_trace_obj_negative_no_running_obj(self):
        """
        Given an invalid RunningObject,
        When Trace.run_file is called with these parameters,
        Then it should raise an exception with an appropriate error message.
        """

        with self.assertRaises(Exception) as error:
            self.parser.trace_obj("Not valid")
        self.assertTrue(
            "Given object 'Not valid' is not callable." in str(error.exception)
        )

    def test_trace_run_file_positive_multiple_runs(self):
        """
        Given a valid module path and a callable function "test",
        When Trace.trace_obj is called twice with these parameters,
        Then it should trace the functions individually and produce the expected trace result for each run.
        """
        module_path = ModuleObject(Path(self.mock_path + "/module_testing_1.py"))
        module_running_obj_1 = RunningObject(module_path, "test()")
        module_running_obj_2 = RunningObject(module_path, "test2()")
        self.parser.trace_obj(module_running_obj_1)
        self.parser.trace_obj(module_running_obj_2)
        expected_trace = r"Trace object\nrunned objects:\n    __init__ + \n    func1 + \n    func2 + \n    test2 + \n    "
        self.assertEqual(expected_trace, repr(self.parser))
