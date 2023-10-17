import sys


class Display:
    def __init__(self, detailed_data, functions_flow):
        self.detail_data = detailed_data
        self.functions_flow = functions_flow

        if self.detail_data.get("<module>"):
            del self.detail_data["<module>"]

        self.ansi_for_tree = {
            "MAIN_OBJECT_ANSI": "\033[38;5;208m",
            "RESET": "\x1b[0m",
            "VERTICAL_LINE": "\u2502",
            "Regular_line": "\u2500",
            "CHILD_OBJECT_ANSI": "\033[36m",
        }

    def tree(self):
        position = 0

        for i in self.functions_flow:
            connector_root = (
                "    "
                + self.ansi_for_tree["MAIN_OBJECT_ANSI"]
                + i
                + self.ansi_for_tree["RESET"]
                + "\n"
            )
            lines = (
                "\n    "
                + self.ansi_for_tree["VERTICAL_LINE"]
                + (self.ansi_for_tree["Regular_line"] * 2)
            )
            connect_branch = (
                lines
                + self.ansi_for_tree["CHILD_OBJECT_ANSI"]
                + f"{position}. "
                + i
                + "\n"
                + self.ansi_for_tree["RESET"]
            )

            connector_display = connector_root if position == 0 else connect_branch

            sys.stdout.write(connector_display)

            if position == (len(self.functions_flow) - 1):
                return

            sys.stdout.write(str("    " + self.ansi_for_tree["VERTICAL_LINE"]))
            sys.stdout.flush()
            position += 1

        # add recursion

    def detailed_data(self, target=""):
        for i in self.detail_data.items():
            display_message = (
                str(i) if not target else (f"{target}: {self.detail_data[target]}")
            )
            sys.stdout.write(display_message)
            sys.stdout.flush()
