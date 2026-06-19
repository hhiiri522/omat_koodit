#!/bin/python3#
import turtle
import random
ruutu = turtle.getscreen()
ruutu.bgcolor("turquoise")

turtle.penup()
turtle.goto(0,180)
turtle.write("KILPIKONNIEN JUOKSUKILPAILU", align="center")
turtle.hideturtle()

# TEKEE MAALIVIIVAN
maali = turtle.Turtle() 
maali.pensize(5)
maali.penup()
maali.goto(180,180)
maali.pendown()
maali.goto(180,-180)
maali.hideturtle()
# LUO 4 PELAAJAA
a = turtle.Turtle()
a.shape("turtle")
a.color("magenta")
a.penup()
a.goto(-180,120)
a.pendown()

b = turtle.Turtle()
b.shape("turtle")
b.color("green")
b.penup()
b.goto(-180,40)
b.pendown()

c = turtle.Turtle()
c.shape("turtle")
c.color("blue")
c.penup()
c.goto(-180,-40)
c.pendown()

d = turtle.Turtle()
d.shape("turtle")
d.color("yellow")
d.penup()
d.goto(-180,-120)
d.pendown()

vauhti1 = random.randint(3,7)
vauhti2 = random.randint(3,7)
vauhti3 = random.randint(3,7)
vauhti4 = random.randint(3,7)

while True:
  a.fd(vauhti1)
  b.fd(vauhti2)
  c.fd(vauhti3)
  d.fd(vauhti4)