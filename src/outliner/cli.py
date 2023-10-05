import argparse
from .outliner import Outliner


def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file_path", help="Path to the file you want to trace", required=True
    )
    parser.add_argument(
        "--object_name",
        help="The name of the object you want to trace",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--object_args",
        help="A list with the argumments required to run the object",
        action="append",
        type=str,
        required=False,
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
        args.object_args[0].split() if args.object_args else None,
        args.display,
    )

    instance_class.run()
