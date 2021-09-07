from random import randint
from time import sleep
from sense_hat import SenseHat

## Lab 4 5a
def print_colours():
    sense = SenseHat()
    for colour in [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255)]:
        sense.set_pixel(randint(0, 7), randint(0, 7), colour)

    sleep(10)
    sense.clear()

print_colours()
