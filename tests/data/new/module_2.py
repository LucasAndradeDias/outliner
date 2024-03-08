def calculate_area(shape_type, dimensions):
    if shape_type == "square":
        return dimensions[0] * dimensions[0]
    elif shape_type == "rectangle":
        return dimensions[0] * dimensions[1]
    elif shape_type == "triangle":
        base = dimensions[0]
        height = dimensions[1]
        return 0.5 * base * height
    else:
        raise ValueError("Invalid shape type")
