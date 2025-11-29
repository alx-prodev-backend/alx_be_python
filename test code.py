# def area_of_triangle (base, height):
#     return (base/2) *height
# test_data = [(2.5, 5.3), # float values
#              (2,5),  #Integre value
#              (True, 6), # boolean value
#              (0, 15 ), # value zero
#              ("base", 5)] # String Value
# for data in test_data:
#     print(f"the area of triangle with {data}"
#           f"is : {area_of_triangle(*data)}")


# another code enhancement  also robust
def area_of_triangle(base: float, height: float) -> float:
    """Calculate the area of a triangle given non-negative numbers."""

    # Validate numeric type (exclude bool)
    if not isinstance(base, (int, float)) or isinstance(base, bool):
        raise TypeError("base must be a real number (int or float).")
    if not isinstance(height, (int, float)) or isinstance(height, bool):
        raise TypeError("height must be a real number (int or float).")

    # Validate positive values
    if base < 0:
        raise ValueError("base must be a non-negative number.")
    if height < 0:
        raise ValueError("height must be a non-negative number.")

    return (base * height) / 2


# Test data
test_data = [
    (2.5, 5.3),    # float
    (2, 5),        # int
    (True, 6),     # bool -> error
    (0, 15),       # zero
    ("base", 5)    # string -> error
]

for data in test_data:
    try:
        result = area_of_triangle(*data)
        print(f"Area of triangle {data} = {result}")
    except Exception as e:
        print(f"Error for input {data}: {e}")


