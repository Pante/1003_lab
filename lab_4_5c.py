from time import sleep
from random import choice, randint
from sense_hat import SenseHat


# Lab 4 5c
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

    while True:
        colour = (randint(0, 255), randint(0, 255), randint(0, 255))
        image = [colour if pixel == y else b for pixel in choice(images)]
        sense.set_pixels(image)
        sleep(1)


# Flat maps the matrix into a list
def flatten(matrix):
    return [pixel for row in matrix for pixel in row]


# Rotates the matrix 90 degree anti-clockwise
def rotate(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]


print_rotating_image()