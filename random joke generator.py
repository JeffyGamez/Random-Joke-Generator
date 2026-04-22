import time 
import random
import math
print ("This repo was made by jeffygamez")
print ("now loading")
time.sleep (5)
print ("Welcome To Random Joke Generator version 1.3.2")

jokes = [
"Why did the chicken cross the road? To run from the KFC"
"Have you heard the rumor of the margarin? Never mind I butter not spread it"
"What did the eraser say to the pencil? You're lookin mighty sharp today"
]
keep_playing = "yes"

while keep_playing == "yes" or keep_playing == "Yes":
  joke_selected = random.choice ( jokes ) 

  print ("Selecting Random Joke.")
 
  time.sleep (3)

  print (f"Random Joke is: {joke_selected}")  

  valid_input = False:
  while valid_input = False: 
    keep_playing = input ("Would You Like To Keep Playing Yes/No")
  
    if keep_playing == "Yes" or keep_playing == "yes":
      valid_input = True
      continue
    elif keep_playing == "No" or keep_playing == "no":
      print ("Goodbye Thank You For Using Random Joke Generator Version 1.3.2 By JeffyGamez")
      valid_input = True
      break
    else:
      print ("ERROR, Invalid Input!")
      
  



