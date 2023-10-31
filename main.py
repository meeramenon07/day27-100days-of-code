print("Character Builder")
import random
import os
import time
def rollDice(side):
 result = random.randint(1,side)
 return result
def health():
  healthStat = ((rollDice(6) * rollDice(12))/2) + 10
  return healthStat
def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2) + 12
  return strengthStat
while True:
  print("Character Builder")
  print()
  name = input("Name your Legend: \n")
  type = input("Character type (Human,Elf,Wizard,Orc):\n")
  print()
  print(name)
  print("Health:", health())
  print("Strength:", strength())
  playAgain = input("play again? : \n")
  if playAgain == "No" or playAgain == "no":
      break
      time.sleep(1)
      os.system("clear")
 

  


#Character Builder

#Name Your Legend:
#Sheila the Almighty

#Character Type (Human, Elf, Wiard, Orc):
#Human
