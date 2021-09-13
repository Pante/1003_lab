# lab 5 5a & 5b

def get_color(color):
    for i in range(3):
        value = input(f"Enter the value of the {color} color for message (0 to 255): ")
        try:
            value = int(value)
            if 0 <= value <= 255:
                return value

            print(f"The given integer, {value} is not between 0 and 255")

        except ValueError:
            print(f"The given value, {value} is not a integer")

    return 0


print(f"returned {get_color('red')}")
