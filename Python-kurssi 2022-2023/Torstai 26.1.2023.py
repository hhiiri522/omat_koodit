#!/bin/python3#
import turtle
import random

# Nämä pitää tehdä, jotta voimme koodailla turtlea.
ruutu = turtle.getscreen()
ruutu.bgcolor("lightblue")
turtle.penup()
turtle.goto(0,190)
turtle.write("Kilpikonnapeli", align="center")

# Alla oleva koodi tekee maaliviivan.
maali = turtle.Turtle()
maali.penup()
maali.pensize(5)
maali.goto(150,180)
maali.pendown()
maali.goto(150,-180)
maali.hideturtle()

# Alla oleva koodi luo pelaajat. Voit keksiä niille myös oikeat nimet.
a = turtle.Turtle()
a.shape("turtle")
a.color("purple")
a.penup()
a.goto(-180,150)
a.pendown()

b = turtle.Turtle()
b.shape("turtle")
b.color("blue")
b.penup()
b.goto(-180,50)
b.pendown()

c = turtle.Turtle()
c.shape("turtle")
c.color("yellow")
c.penup()
c.goto(-180,-50)
c.pendown()

d = turtle.Turtle()
d.shape("turtle")
d.color("green")
d.penup()
d.goto(-180,-150)
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