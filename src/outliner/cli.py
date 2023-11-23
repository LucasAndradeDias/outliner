import argparse
from .outliner import Outliner


def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file_path",
        "-fp",
        help="Path to the file you want to trace",
        required=True,
        nargs=1,
    )
    parser.add_argument(
        "--object_invoke",
        "-o",
        help="The invoking statement of the object",
        type=str,
        required=True,
        nargs=1,
    )
    parser.add_argument(
        "--mode",
        "-m",
        help="Type of display you want (detailed_data or tree)",
        choices=["tree", "detailed_data"],
        default="tree",
        nargs=1,
    )

    return parser.parse_args()


def main():
    args = parser_arguments()

    instance_class = Outliner(
        args.file_path,
        args.object_name,
        args.display,
    )

    instance_class.run()
