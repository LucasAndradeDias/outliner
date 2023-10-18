import unittest
import collections
import sys

from src.outliner import Display
from unittest.mock import patch
from io import StringIO


functions_flow = collections.OrderedDict(
    [("test2", None), ("__init__", None), ("func1", None), ("func2", None)]
)

detail_data = collections.defaultdict(
    int,
    {
        "test2": {"call": 1, "return": 1, "line": 2},
        "__init__": {"call": 1, "return": 1, "line": 1},
        "func1": {"call": 1, "return": 1, "line": 2},
        "func2": {"call": 1, "return": 1, "line": 1},
    },
)

detail_data_with_exception = collections.defaultdict(
    int,
    {
        "test2": {"call": 1, "return": 1, "line": 2},
        "__init__": {"call": 1, "return": 1, "line": 1},
        "func1": {"call": 1, "return": 1, "line": 2},
        "func2": {"call": 1, "return": 1, "line": 1, "exception": 1},
    },
)


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.parser = Display(detail_data, functions_flow)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_tree_positive_input(self, stdout):
        expected_result = "    \x1b[38;5;208mtest2\x1b[0m\n    │\n    │──\x1b[36m1. __init__\n\x1b[0m    │\n    │──\x1b[36m2. func1\n\x1b[0m    │\n    │──\x1b[36m3. func2\n\x1b[0m"
        self.parser.tree()
        self.assertEqual(stdout.getvalue(), expected_result)

    @patch("src.outliner.Display")
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_tree_with_no_data(self, stdout, module):
        running = module({}, {})
        running.tree()
        self.assertEqual("", stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_detailed_data_positive_input(self, stdout):
        expected_result = "('test2', {'call': 1, 'return': 1, 'line': 2})('__init__', {'call': 1, 'return': 1, 'line': 1})('func1', {'call': 1, 'return': 1, 'line': 2})('func2', {'call': 1, 'return': 1, 'line': 1})"

        self.parser.detailed_data()
        self.assertEqual(expected_result, stdout.getvalue())

    @patch("src.outliner.Display")
    @patch("sys.stdout", new_callable=StringIO)
    def test_detailed_data_negative_input(self, stdout, module):
        module_instance = module({}, {})
        module_instance.detailed_data()
        self.assertEqual("", stdout.getvalue())

    @patch("src.outliner.Display")
    @patch("sys.stdout", new_callable=StringIO)
    def test_func_with_exception(self, stdout, module):
        expected_result = "    \x1b[38;5;208mtest2\x1b[0m\n    │\n    │──\x1b[36m1. __init__\n\x1b[0m    │\n    │──\x1b[36m2. func1\n\x1b[0m    │\n    │──\x1b[33m3. func2\n\x1b[0m"
        module_instance = module()
        module_instance.tree()
        self.assertEqual("", stdout.getvalue())
