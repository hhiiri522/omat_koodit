#!/bin/python3#
import turtle

ruutu = turtle.Screen()
ruutu.bgcolor("lightblue")

tipi = turtle.Turtle()
tipi.shape("turtle")
tipi.hideturtle()

print("Kirjoita, mitä haluat.")
kysymys = input("Mitä haluat kirjoittaa? ")
tipi.write(kysymys)