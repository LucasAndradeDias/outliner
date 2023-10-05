import unittest
import collections
import sys

from pathlib import Path
from outliner import Trace
from unittest.mock import patch
from io import StringIO


class test_trace(unittest.TestCase):
    def setUp(self):
        self.base_path = Path(__file__).resolve()
        self.mock_path = str(self.base_path.parent / "data")
        self.parser = Trace()

    def tearDown(self):
        self.parser.detailed_data = collections.defaultdict(
            lambda: {"call": 0, "return": 0, "line": 0}
        )
        self.parser.functions_flow = collections.OrderedDict()

    def test_run_file_positive_input(self):
        """
        Given a valid module path and a callable function "test",
        When Trace.run_file is called with these parameters,
        Then it should trace the function and produce the expected trace result.
        """
        module_path = self.mock_path + "/module_testing_1.py"
        self.parser.run_file(module_path, "test")
        expected_trace = r"Trace object\nrunned objects:\n    __init__ + \n    func1 + \n    func2 + \n    "
        self.assertEqual(expected_trace, repr(self.parser))

    def test_run_file_positive_input_with_parameters(self):
        """
        Given a valid module path, a callable function "numberToIp",
        and function parameters ["000"],
        When Trace.run_file is called with these parameters,
        Then it should trace the function and produce the expected trace result.
        """
        module_path = self.mock_path + "/module_testing_2.py"
        self.parser.run_file(module_path, "numberToIp", ["000"])

        expected_trace = (
            r"Trace object\nrunned objects:\n    numberToIp + \n    <listcomp> + \n    "
        )

        self.assertEqual(expected_trace, repr(self.parser))

    def test_trace_run_file_negative_no_module(self):
        """
        Given an invalid module path,
        When Trace.run_file is called with these parameters,
        Then it should raise an exception with an appropriate error message.
        """
        with self.assertRaises(Exception) as error:
            self.parser.run_file("not_valid_path", "object")
        self.assertTrue("Error on the execution of the module" in str(error.exception))

    def test_trace_run_file_file_negative_non_callable_object(self):
        """
        Given a valid module path and a non-callable object "non_callable",
        When Trace.run_file is called with these parameters,
        Then it should raise an exception with an appropriate error message.
        """
        module_path = (
            self.mock_path + "/module_testing_2.py"
        )  # Contains a non-callable object
        with self.assertRaises(Exception) as error:
            self.parser.run_file(module_path, "non_callable")
            self.assertEqual(
                "Object 'non_callable' not found in module" in str(error.exception)
            )

    def test_trace_run_file_positive_multiple_runs(self):
        """
        Given a valid module path and a callable function "test",
        When Trace.run_file is called twice with these parameters,
        Then it should trace the functions individually and produce the expected trace result for each run.
        """
        module_path = self.mock_path + "/module_testing_1.py"
        self.parser.run_file(module_path, "test")
        self.parser.run_file(module_path, "test2")
        expected_trace = r"Trace object\nrunned objects:\n    __init__ + \n    func1 + \n    func2 + \n    test2 + \n    "
        self.assertEqual(expected_trace, repr(self.parser))


if __name__ == "__main__":
    unittest.main()
