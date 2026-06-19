#!/bin/python3#
import random
import time

pistemaara = 0

while True:
  arpoja = random.randint(1,2)
  print(arpoja)
  if arpoja == 1:
    print("hyppää")
    pistemaara = pistemaara+2
    print("Pistemääräsi:",pistemaara)
    time.sleep(1)
  elif arpoja == 2:
    print("juoksee")
    time.sleep(1)