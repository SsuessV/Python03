import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input("Enter new coordinates"
                            " as floats in format 'x,y,z': ")
        list_coordinates = coordinates.split(",")

        if len(list_coordinates) != 3:
            print("Invalid syntax")
            continue

        try:
            x, y, z = list_coordinates
            float_x = float(x)
            float_y = float(y)
            float_z = float(z)
            return (float_x, float_y, float_z)

        except ValueError as e:
            for value in list_coordinates:
                try:
                    float(value)
                except ValueError:
                    print(f"Error on parameter '{value}': {e}")
                    break


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first_set = get_player_pos()
    x, y, z = first_set
    print(f"Got a first tuple: {first_set}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    distance = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance to center: {distance:.4f}")
    print()
    print("Get a second set of coordinates")
    second_set = get_player_pos()
    x2, y2, z2 = second_set
    distance_2 = math.sqrt((x2 - x)**2 + (y2 - y)**2 + (z2 - z)**2)
    print(f"Distance between the 2 sets of coordinates: {distance_2:.4f}")
