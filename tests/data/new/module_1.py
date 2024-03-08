from module_2 import calculate_area
from module_3 import DataProcessor


class Shape:
    def __init__(self, shape_type, dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def calculate_area(self):
        area = calculate_area(self.shape_type, self.dimensions)


def main():
    shapes = [
        Shape("square", [5]),
        Shape("rectangle", [3, 4]),
        Shape("triangle", [2, 6]),
    ]

    for shape in shapes:
        shape.calculate_area()

    processor = DataProcessor()
    data = processor.load_data("sample_data.txt")
    processor.analyze_data(data)
