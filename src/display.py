import pprint


class Display:
    def __init__(self, detailed_data, functions_flow):
        self.detail_data = detailed_data
        self.functions_flow = functions_flow

        if self.detail_data.get("<module>"):
            del self.detail_data["<module>"]

    def tree(self):
        position = 0
        for i in self.functions_flow:
            connector2 = "  " + "|" + "---" * position if position != 0 else ""
            print(connector2 + f" {i}()")
            position += 1
        return
        # add recursion

    def detailed_data(self, target=""):
        for i in self.detail_data.items():
            pprint.pprint(
                i if not target else (f"{target}: {self.detail_data[target]}")
            )
        return
