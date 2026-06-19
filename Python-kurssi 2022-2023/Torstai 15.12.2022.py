#!/bin/python3 # KIRJOITA KOODISI RIVILTÄ 2 ALKAEN
import turtle

ruutu = turtle.Screen()
ruutu.bgcolor("lightblue")

tipi = turtle.Turtle()
tipi.shape("turtle")
tipi.color("blue")
tipi.speed(100)

tipi.begin_fill()

for kierros in range(5):
  tipi.fd(150)
  tipi.right(144)
  
tipi.end_fill()

tipi.penup()
tipi.goto(-130,130)

tipi.end_fill()

tipi.begin_fill()

for kierros in range(5):
  tipi.pendown()
  tipi.fd(150)
  tipi.rt(144)
  
tipi.fillcolor("yellow")
tipi.end_fill()
  
tipi.penup()
tipi.goto(-120,-120)
tipi.pendown()

tipi.begin_fill()

for kierros in range(5):
  tipi.fd(80)
  tipi.rt(144)
  
tipi.fillcolor("red")
tipi.end_fill()