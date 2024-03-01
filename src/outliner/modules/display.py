import sys


class Display:
    def __init__(self, detailed_data: dict, functions_flow: dict):
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
            "CHILD_WITH_EXECEPTION": "\033[31m",
        }

    def tree(self):
        for position, func in enumerate(self.functions_flow):
            func_With_exception = bool(self.detail_data[func].get("exception"))

            connector_root = (
                "    "
                + self.ansi_for_tree["MAIN_OBJECT_ANSI"]
                + func
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
                + self.ansi_for_tree[
                    (
                        "CHILD_OBJECT_ANSI"
                        if not func_With_exception
                        else "CHILD_WITH_EXECEPTION"
                    )
                ]
                + f"{position}. "
                + func
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

    def detailed_data(self, target=""):
        found_funcs_messages = []

        for key, value in self.detail_data.items():
            func_message = f"{key}\n   called: {value.get('call')}\n   return: {value.get('return')}\n   lines: {value.get('line')}\n"
            found_funcs_messages.append(func_message)

        display_message = "\n".join(sorted(found_funcs_messages))

        sys.stdout.write(f"\nInvoked objects: {len(self.detail_data.items())}\n\n")
        sys.stdout.write(display_message)
        sys.stdout.flush()
