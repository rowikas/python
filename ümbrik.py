from turtle import *
from math import sqrt
ümbrik = int(input("Sisesta mingi täisarv: "))
ümbrik_a = sqrt(2 * ümbrik ** 2)

forward(ümbrik)
left(135)
forward(ümbrik_a)
right(90)
forward((ümbrik_a / 2))
right(90)
forward((ümbrik_a / 2))
right(90)
forward(ümbrik_a)
right(135)
forward(ümbrik)
right(90)
forward(ümbrik)
right(90)
forward(ümbrik)
exitonclick()
