from time import sleep
from random import choice
from sense_hat import SenseHat


# Lab 4 5b
def print_rotating_image():
    sense = SenseHat()
    r = (255, 0, 0)
    y = (255, 255, 0)
    b = (0, 0, 0)

    original = [[b, b, b, b, b, b, b, b],
                [b, b, b, y, b, b, b, b],
                [b, b, y, y, y, b, b, b],
                [b, y, b, y, b, y, b, b],
                [b, b, b, y, b, b, b, b],
                [b, b, b, y, b, b, b, b],
                [b, b, b, y, b, b, b, b],
                [b, b, b, b, b, b, b, b]]

    # This section can technically be more optimal if we cache the resultant matrix of each rotation but I'm lazy
    images = [
        flatten(original),
        flatten(rotate(original)),
        flatten(rotate(rotate(original))),
        flatten(rotate(rotate(rotate(original))))
    ]

    current = y
    while True:
        image = choice(images)
        colored = image if current == y else [r if pixel == y else b for pixel in image]
        current = r if current == y else y
        sense.set_pixels(colored)
        sleep(1)


# Flat maps the matrix into a list
def flatten(matrix):
    return [pixel for row in matrix for pixel in row]


# Rotates the matrix 90 degree anti-clockwise
def rotate(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]


print_rotating_image()
