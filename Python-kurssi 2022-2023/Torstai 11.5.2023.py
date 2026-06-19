#!/bin/python3#
import turtle
ruutu = turtle.Screen()
ruutu.bgcolor("turquoise")
ruutu.addshape("rocketship.gif")

tipi = turtle.Turtle()
tipi.shape("rocketship.gif")
tipi.penup()

def koordi(x,y):
  tipi.setheading(tipi.towards(x,y))
  tipi.goto(x,y)

ruutu.onclick(koordi)