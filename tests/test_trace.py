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
        self.parser.detailed_data = collections.defaultdict()
        self.parser.functions_flow = collections.OrderedDict()

    def test_run_positive_input(self):
        module_path = self.mock_path + "/module_testing_1.py"
        self.parser.run(module_path, "test")
        expected_trace = r"Trace object\nrunned objects:\n    __init__ + \n    func1 + \n    func2 + \n    "
        self.assertEqual(expected_trace, repr(self.parser))

    def test_run_positive_input_with_parameters(self):
        module_path = self.mock_path + "/module_testing_2.py"
        self.parser.run(module_path, "numberToIp", ["000"])

        expected_trace = (
            r"Trace object\nrunned objects:\n    numberToIp + \n    <listcomp> + \n    "
        )

        self.assertEqual(expected_trace, repr(self.parser))

    def test_run_negative_no_module(self):
        with self.assertRaises(Exception) as error:
            self.parser.run("not valid path", "object")


if __name__ == "__main__":
    unittest.main()
