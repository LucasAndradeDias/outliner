import argparse
from .outliner import Outliner  # Import functions from your library


def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", required=True)
    parser.add_argument("--object_type", required=False)
    parser.add_argument("--object_name", type=str, required=True)
    parser.add_argument("--object_args", action="append", type=str, required=False)
    return parser.parse_args()


def main():
    args = parser_arguments()

    instance_class = Outliner(
        args.file_path,
        args.object_name,
        args.object_args[0].split() if args.object_args else None,
    )

    instance_class.run()
