import random
roll="yes"
while roll=="yes" or roll=="y" :
  print("Dice rolling...")
  print("you have diced "+str( random.randint(1,6)))
  roll=raw_input("roll again?")
