from turtle import *

speed(4)
shape("arrow")

pensize:10

sides = 5
length = 100
angle = 144

# pentagon
for count in range (sides):
    forward(length)
    right(angle)

stop = input("x")