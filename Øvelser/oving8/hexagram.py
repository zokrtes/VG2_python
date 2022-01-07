from turtle import *

speed(4)
shape("arrow")

pensize:10

sides = 6
length = 100
angle = 60

# hexagram
for count in range (sides):
    forward(length)
    right(angle)

stop = input("x")