#importing random and time
import random
import time
import os
from images import picture
from images import picture2

#clearing the console
clear = lambda: os.system('clear')


def challenger():
  y = 0
  t = "...\n"
  while y <= len(t):
    clear()
    print(t[:y])
    time.sleep(0.2)
    y = y + 1
  time.sleep(0.5)

def problem():
  m = 0
  n = "OhNo...ItSeEmS...ThERe...IS...a...PrOBlEM\n"
  while m <= len(n):
    clear()
    print(n[:m])
    time.sleep(0.05)
    m += 1
    time.sleep(0.05)
  
#variable token
token = 1


#defining countdown
def countdown(t):
  while t:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1


t = str(5)


#tokens loops
if token >= 1:
  answer = str(
    input(
      f"You have {token} token, would you like to use 1 token to play?: (Yes, or No) "
    ))
elif token <= 0:
  print(token)
  print("You are illegible to play, run the repl again :)")
  

  #asking for play
  if answer == "Yes" or answer == "yes":
    token -= 1
    print(f"You have {token} tokens left.")
  elif answer == "No" or answer == "no":
    print("See you again next time!")
    exit()
  elif token < 1:
    print("Sorry you can not play :(")
    exit()
  else:
    print("Sorry to see you go :(")
    exit()

challenger()

#age input
clear()
age = int(input('How old are you?: '))
time.sleep(1)

#you need to be alive to play
if age <= 0:
  print("you are not born, die and suffer! :)")
  exit()

#allowes for computer to be "thinking"
challenger()

clear()
name = str(input('What is your name?: '))
time.sleep(1)

#allows for computer to be "thinking"
challenger()

#gender input
clear()
gender = str(input('What is your gender? ( F for Female, M for Male ): '))
time.sleep(1)

#causing a break in console
challenger()

#all random numbers for users
Mrand1 = random.randint(1, 10)
Mrand2 = random.randint(1, 7)
Mrand3 = random.randint(1, 5)
Frand1 = random.randint(1, 10)
Frand2 = random.randint(1, 7)
Frand3 = random.randint(1, 5)

#males over 18
if age > 18:
  if gender == "M" or gender == "m":
    clear()
    print(f"Hello Mr {name}, we will pick a number for you from 1 - 10...")
    print('Your number is: ', end='')
    print(Mrand1)
  elif gender == "F" or gender == "m":
    clear()
    print(f"Hello Mrs {name}, we will pick a number for you from 1 to 10")
    print('Your number is: ', end='')
    print(Frand1)
  else:
    print("That seems unfamiliar")
    time.sleep(1)
    problem()
    exit()
  time.sleep(2.5)
  clear()

#males 18
elif age == 18:
  if gender == "M" or gender == "m":
    clear()
    print(f"Hi Master {name}, we will pick a number for you from 1 to 7")
    print('Your number is: ', end='')
    print(Mrand2)
  elif gender == "F" or gender == "f":
    clear()
    print(f"Hi Miss {name}, we will pick a number for you from 1 to 7")
    print('Your number is: ', end='')
    print(Frand2)
  else:
    print("That seems unfamiliar")
    time.sleep(1)
    problem()
    exit()
  time.sleep(2.5)
  clear()

  #males under 18
elif age < 18:
  if gender == "M" or gender == "m":
    clear()
    print("Hi Little Boy, we will pick a number for you from 1 to 5")
    print('Your number is: ', end='')
    print(Mrand3)
  elif gender == "F" or gender == "f":
    clear()
    print("Hi Little Girl, we will pick a number for you from 1 to 5")
    print('Your number is: ', end='')
    print(Frand3)
  else:
    print("That seems unfamiliar")
    time.sleep(1)
    problem()
    exit()
  time.sleep(2.5)
  clear()

#choices list
prizes = ["1 token", "2 tokens", "0 tokens", "Irtaza's Glasses"]

#random prize chosen if won
prize1 = random.randint(1, 10)
prize2 = random.randint(1, 7)
prize3 = random.randint(1, 5)

countdown(int(t))
clear()
#congratulations speeches
if Mrand1 == prize1:
  print(f"Congratulations {name} you won {random.choice(prizes)}")
  if prizes == "1 token":
    token += 1
  elif prizes == "2 tokens":
    token += 2
  else:
    token = token
  for image in picture:
    for pixels in image:
      if (pixels):
        print('*', end="")
      else:
        print(' ', end="")
    print('')

elif Mrand2 == prize2:
  print(f"Congratulations {name} you won {random.choice(prizes)}")
  if prizes == "1 token":
    token += 1
  elif prizes == "2 tokens":
    token += 2
  else:
    token = token
  for image in picture:
    for pixels in image:
      if (pixels):
        print('*', end="")
      else:
        print(' ', end="")
    print('')
elif Mrand3 == prize3:
  print(" ")

  print(f"Congratulations {name} you won {random.choice(prizes)}")
  if prizes == "1 token":
    token += 1
  elif prizes == "2 tokens":
    token += 2
  else:
    token = token
  for image in picture:
    for pixels in image:
      if (pixels):
        print('*', end="")
      else:
        print(' ', end="")
    print('')

elif Frand1 == prize1:
  print(f"Congratulations {name} you won {random.choice(prizes)}")
  if prizes == "1 token":
    token += 1
  elif prizes == "2 tokens":
    token += 2
  else:
    token = token
  for image in picture:
    for pixels in image:
      if (pixels):
        print('*', end="")
      else:
        print(' ', end="")
    print('')

elif Frand2 == prize2:
  print(f"Congratulations {name} you won {random.choice(prizes)}")
  if prizes == "1 token":
    token += 1
  elif prizes == "2 tokens":
    token += 2
  else:
    token = token
  for image in picture:
    for pixels in image:
      if (pixels):
        print('*', end="")
      else:
        print(' ', end="")
    print('')

elif Frand3 == prize3:
  print(f"Congratulations {name} you won {random.choice(prizes)}")
  if prizes == "1 token":
    token += 1
  elif prizes == "2 tokens":
    token += 2
  else:
    token = token
  for image in picture:
    for pixels in image:
      if (pixels):
        print('*', end="")
      else:
        print(' ', end="")
    print('')

else:
  print(f"Sorry {name}, you did not win! :(")
  print(" ")
  for image2 in picture2:
    for pixels2 in image2:
      if (pixels2):
        print('*', end="")
      else:
        print(' ', end="")
    print('')