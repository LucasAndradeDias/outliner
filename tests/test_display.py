import unittest
import collections
import sys

from pathlib import Path 
from src.outliner import Display
from unittest.mock import patch
from io import StringIO


PATH = Path(str(Path(__file__).resolve() / "data" ) + "/module_testing_1.py")

functions_flow = collections.OrderedDict(
    [("test2", None), ("__init__", None), ("func1", None), ("func2", None)]
)

detail_data = collections.defaultdict(
    int,
    {
        "test2": {"call": 1, "return": 1, "line": 2, "file": PATH, "start_line": 13},
        "__init__": {"call": 1, "return": 1, "line": 1, "file": PATH, "start_line": 2},
        "func1": {"call": 1, "return": 1, "line": 2, "file": PATH, "start_line": 5},
        "func2": {"call": 1, "return": 1, "line": 1, "file": PATH, "start_line": 9},
    },
)

detail_data_with_exception = collections.defaultdict(
    int,
    {
        "test2": {"call": 1, "return": 1, "line": 2, "file": PATH, "start_line": 13},
        "__init__": {"call": 1, "return": 1, "line": 1, "file": PATH, "start_line": 2},
        "func1": {"call": 1, "return": 1, "line": 2, "file": PATH, "start_line": 5},
        "func2": {"call": 1, "return": 1, "line": 1, "exception": 1, "file": PATH, "start_line": 9},
    },
)


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.parser = Display(detail_data, functions_flow)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_tree_positive_input(self, stdout):
        expected_result = "    \x1b[38;5;208mtest2\x1b[0m\n    │\n    │──\x1b[36m1. __init__                                          module_testing_1.py     2\n\x1b[0m    │\n    │──\x1b[36m2. func1                                             module_testing_1.py     5\n\x1b[0m    │\n    │──\x1b[36m3. func2                                             module_testing_1.py     9\n\x1b[0m"
        self.parser.tree()
        self.assertEqual(repr(stdout.getvalue()), repr(expected_result))

    @patch("src.outliner.Display")
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_tree_with_no_data(self, stdout, module):
        running = module({}, {})
        running.tree()
        self.assertEqual("", stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_detailed_data_positive_input(self, stdout):
        expected_result = "\nInvoked objects: 4\n\n__init__\n   called: 1\n   return: 1\n   lines: 1\n\nfunc1\n   called: 1\n   return: 1\n   lines: 2\n\nfunc2\n   called: 1\n   return: 1\n   lines: 1\n\ntest2\n   called: 1\n   return: 1\n   lines: 2\n"

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
        module_instance = module()
        module_instance.tree()
        self.assertEqual("", stdout.getvalue())
