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
            x = float(list_coordinates[0])
            y = float(list_coordinates[1])
            z = float(list_coordinates[2])
            return (x, y, z)
        except ValueError as e:
            for list_coordinate in list_coordinates:
                try:
                    float(list_coordinate)
                except ValueError:
                    print(f"Error on parameter '{list_coordinate}': {e}")
                    break


print("=== Game Coordinate System ===")
print()
print("Get a first set of coordinates")
first_set = get_player_pos()
print(f"Got a first tuple: {first_set}")
print(f"It includes: X={first_set[0]}, Y={first_set[1]}, Z={first_set[2]}")
distance = math.sqrt(first_set[0]**2 + first_set[1]**2 + first_set[2]**2)
print(f"Distance to center: {distance:.4f}")
print()
print("Get a second set of coordinates")
second_set = get_player_pos()
distance_2 = math.sqrt((second_set[0] - first_set[0])**2 +
                       (second_set[1] - first_set[1])**2 +
                       (second_set[2] - first_set[2])**2)
print(f"Distance between the 2 sets of coordinates: {distance_2:.4f}")
