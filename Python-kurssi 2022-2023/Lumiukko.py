#!/bin/python3 # KIRJOITA KOODISI RIVILTÄ 2 ALKAEN
import turtle

ruutu = turtle.Screen()
ruutu.bgcolor("lightblue")

tipi = turtle.Turtle()
tipi.shape("turtle")
tipi.color("white")
tipi.speed(100)

tipi.begin_fill()

tipi.goto(0,50)
tipi.circle(20)

tipi.home()
tipi.circle(25)

tipi.goto(0,-70)
tipi.circle(35)

tipi.end_fill()

tipi.penup()
tipi.color("orange")
tipi.goto(0,75)
tipi.pendown()
tipi.goto(0,50)
tipi.penup()
tipi.goto(0,90)

tipi.color("black")
tipi.pendown()
tipi.goto(50,90)
tipi.left(90)
tipi.fd(50)
tipi.left(90)
tipi.fd(25)
tipi.right(90)
tipi.fd(25)
tipi.left(90)
tipi.fd(50)

tipi.left(90)
tipi.fd(25)
tipi.right(90)
tipi.fd(25)
tipi.left(90)
tipi.fd(50)
tipi.left(90)
tipi.fd(50)
tipi.end_fill()
tipi.hideturtle()