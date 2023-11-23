import argparse
from .outliner import Outliner


def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file_path", help="Path to the file you want to trace", required=True
    )
    parser.add_argument(
        "--object_invoke",
        help="The invoking statement of the object",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--display",
        "-d",
        help="Select the type of display you want",
        choices=["tree", "detailed_data"],
        default="tree",
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
