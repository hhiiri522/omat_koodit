#!/bin/python3 #
import turtle
import os
import random
import time

# LUO PELIRUUTU
ikkuna = turtle.Screen()
ikkuna.setup(width= 440, height= 550)
ikkuna.bgcolor("lightblue")
ikkuna.tracer(0)

# LUO PELAAJA
tipi = turtle.Turtle()
tipi.shape("arrow")
tipi.color("yellow")
tipi.left(90)
tipi.penup()
tipi.goto(0,-230)
tipi.direction = "stop"

# LUO PISTEET JA ELÄMÄT
pisteet = 0
elamat = 3

# LUODAAN HYVÄT ASIAT
hyvalista = []

for h in range(10):
  hyva = turtle.Turtle()
  hyva.shape("circle")
  hyva.color("green")
  hyva.penup()
  hyva.goto(random.randint(-200,200), random.randint(300,600))
  hyva.speed = random.randint(1,2)
  
  hyvalista.append(hyva)
  
# LUODAAN HUONOT ASIAT
huonolista = []

for h in range(10):
  huono = turtle.Turtle()
  huono.shape("circle")
  huono.color("red")
  huono.penup()
  huono.goto(random.randint(-200,200), random.randint(300,600))
  huono.speed = random.randint(1,2)
  
  huonolista.append(huono)

# LUODAAN PISTEIDENLASKU
kyna = turtle.Turtle()
kyna.color("white")
kyna.penup()
kyna.hideturtle()
kyna.goto(0,240)
kyna.write("Pisteet: 0 Elämät: 3", align="center", font=("Arial", 20))

# LUODAAN FUNKTIOT, JOTKA LIIKUTTAVAT PELAAJAA
def vasemmalle():
  tipi.direction = "left"
  
def oikealle():
  tipi.direction = "right"
  
# NÄPPÄIMISTÖN ASETUKSET
ikkuna.listen()
ikkuna.onkey(vasemmalle, "Left")
ikkuna.onkey(oikealle, "Right")

# PELIN TOISTORAKENNE
while True:
  ikkuna.update()
  
  # LIIKUTTAA PELAAJAA
  if tipi.direction == "left":
    tipi.setx(tipi.xcor()-1)
  if tipi.direction == "right":
    tipi.setx(tipi.xcor()+1)
    
  # TARKISTETAAN, TÖRMÄÄKÖ PELAAJA REUNOIHIN
  if tipi.xcor() < -200:
    tipi.setx(-200)
  if tipi.xcor() > 200:
    tipi.setx(200)
    
  # LIIKUTETAAN HYVIÄ PALLOJA
  for hyva in hyvalista:
    hyva.sety(hyva.ycor() - hyva.speed)
    
    # TARKISTETAAN, OVATKO HYVÄT PALLOT RUUDUN ALAPUOLELLA
    if hyva.ycor() < -300:
      hyva.goto(random.randint(-210,210), random.randint(400,800))
      
    # HOIDETAAN TÖRMÄYKSET
    if tipi.distance(hyva) < 25:
      pisteet += 1 # LISÄTÄÄN PISTE
      # SIIRRETÄÄN PALLO TAKAISIN YLHÄÄLLE
      hyva.goto(random.randint(-210,210), random.randint(400,800))
      # PÄIVITETÄÄN PISTEIDENLASKU
      kyna.clear()
      kyna.write("Pisteet: {} Elämät: {}".format(pisteet, elamat), align="center", font=("Arial", 20))
      
    # LIIKUTETAAN HUONOJA PALLOJA
    for huono in huonolista:
      huono.sety(huono.ycor() - huono.speed)
      
      # TARKISTETAAN, OVATKO HUONOT PALLOT RUUDUN ALAPUOLELLA
      if huono.ycor() < -300:
        huono.goto(random.randint(-210,210), random.randint(400,800))
        
      # HOIDETAAN TÖRMÄYKSET
      if tipi.distance(huono) < 25:
        elamat -= 1 # POISTETAAN ELÄMÄ
        time.sleep(0.5)
        # SIIRRETÄÄN PALLO TAKAISIN YLHÄÄLLE
        huono.goto(random.randint(-210,210), random.randint(400,800))
        # PÄIVITETÄÄN PISTEIDENLASKU
        kyna.clear()
        kyna.write("Pisteet: {} Elämät: {}".format(pisteet, elamat), align="center", font=("Arial", 20))
      
      # TARKISTETAAN, ONKO PELI OHI
      if elamat == 0:
        kyna.clear()
        kyna.write("PELI LOPPUI! Pisteet: {}".format(pisteet), align="center", font=("Arial", 20))
        ikkuna.update()
        time.sleep(5)
        pisteet = 0
        elamat = 3
        kyna.clear()
        kyna.write("Pisteet: {} Elämät: {}".format(pisteet, elamat), align="center", font=("Arial", 20))
