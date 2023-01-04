# Remove this comment to confirm that this task is done
from turtle import *

offset = -200, -300


def read_coords():
    coords = []
    with open("dots.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            coords.append(line.split())

        return coords


def connect_the_dots():
    coords = read_coords()
    penup()
    fillcolor("pink")
    begin_fill()
    for coord in coords:
        goto((int(coord[0]) + offset[0]) * (-1), (int(coord[1]) + offset[1]) * (-1))
        dot()
        pendown()
    end_fill()


speed("fastest")
connect_the_dots()
exitonclick()
