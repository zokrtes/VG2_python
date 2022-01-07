from turtle import *

speed(4)
shape("arrow")

pensize:10

sides = 3
length = 100
angle = 120

# trekant
for count in range (sides):
    forward(length)
    right(angle)

stop = input("x")