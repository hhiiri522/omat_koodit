#!/bin/python3#
import turtle
koko = 50
ikkuna = turtle.Screen()
ikkuna.bgcolor("gold")

tipi = turtle.Turtle()
tipi.shape("turtle")
tipi.color("magenta")
tipi.speed(100)
lisaantyva = 101,-100

while True:
  tipi.goto(100,100)
  tipi.goto(-100,100)
  tipi.goto(-100,-100)
  tipi.goto(100,-100)
  tipi.goto(lisaantyva)