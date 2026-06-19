import turtle
ruutu = turtle.Screen()
ruutu.bgcolor("lightblue")
tipi = turtle.Turtle()
tipi.color("magenta")
tipi.shape("turtle")
#tipi.speed(100)
#tipi.pencolor("blue")

def ympyra():
  tipi.circle(50)
  tipi.hideturtle()

kysymys = input("Kirjoita piirrettävän tai kirjoitettavan asian nimi: ")
if kysymys == "ympyrä":
  ympyra()
elif kysymys == "neliö":
  tipi.fd(100)
  tipi.lt(90)
  tipi.fd(100)
  tipi.lt(90)
  tipi.fd(100)
  tipi.lt(90)
  tipi.fd(100)
  tipi.lt(90)
  tipi.hideturtle()

elif kysymys == "kolmio":
  tipi.goto(50,0)
  tipi.goto(0,75)
  tipi.goto(-50,0)
  tipi.goto(0,0)
  tipi.hideturtle()


elif kysymys == "kukka":
  tipi.fillcolor("yellow")
  tipi.begin_fill()
  for kierros in range (6):
    tipi.circle(70)
    tipi.rt(60)
  tipi.end_fill()

  tipi.fillcolor("orange")
  tipi.begin_fill()
  for kierros in range (6):
    tipi.circle(50)
    tipi.rt(60)
  tipi.end_fill()
  
  tipi.fillcolor("red")
  tipi.begin_fill()
  for kierros in range (6):
    tipi.circle(30)
    tipi.rt(60)
  tipi.end_fill()
  
  tipi.fillcolor("white")
  tipi.begin_fill()
  for kierros in range (6):
    tipi.circle(10)
    tipi.rt(60)
  tipi.end_fill()
  
  tipi.hideturtle()


elif kysymys == "pipo":
  tipi.goto(-50,0)
  tipi.goto(0,75)
  tipi.circle(15)
  tipi.goto(50,0)
  tipi.goto(0,0)
  tipi.hideturtle()
  
elif kysymys == "tikku-ukko":
  tipi.circle(30)
  tipi.goto(50,-75)
  tipi.goto(0,0)
  tipi.goto(-50,-75)
  tipi.goto(0,0)
  tipi.goto(50,0)
  tipi.goto(-50,0)
  
else:
  print("Tuollaista et voi valitettavasti piirtää.")