import argparse
import sys

from pathlib import Path
from trace import Trace
from display import Display


def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", required=True)
    parser.add_argument("--object_type", required=False)
    parser.add_argument("--object_name", type=str, required=True)
    parser.add_argument("--object_args", action="append", type=list, required=False)
    return parser.parse_args()


def check_args(args):
    if not Path(args.file_path).is_file():
        raise ("Not a valid file")
    if not ".py" in args.file_path:
        raise ("Not a python file")


def main(args):
    trace = Trace()
    trace.run(args.file_path, args.object_name, args.object_args)
    display_class = Display(trace.detailed_data, trace.functions_flow)
    display_class.tree()


if __name__ == "__main__":
    args = parser_arguments()
    check_args(args)
    main(args)
