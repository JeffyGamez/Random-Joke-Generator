import time 
import random
import math # the import math is not needed at the moment but i may need it for future updates
# This Section is the into to the program
print ("This repo was made by jeffygamez")
print ("now loading")
time.sleep (5)
print ("Welcome To Random Joke Generator version 1.4")
# This section is for all the jokes make sure to put comma's after new jokes and to format it correctly for string text
jokes = [
"Why did the chicken cross the road? To run from the KFC",
"Have you heard the rumor of the margarine? Never mind I butter not spread it",
"What did the eraser say to the pencil? You're lookin mighty sharp today",
"Why don't scientists trust atoms? Because they make up everything!",
"What do you call a fake noodle? An impasta!",
"Why did the scarecrow win an award? He was outstanding in his field!",
"What do you call a sleeping bull? A dozer!",
"Why don't eggs tell jokes? They'd crack each other up!",
"What did the ocean say to the beach? Nothing, it just waved!",
"Why did the math book look sad? Because it had too many problems!"
]
# This is the section that keeps the joke going
keep_playing = "yes"

while keep_playing == "yes" or keep_playing == "Yes":
  joke_selected = random.choice ( jokes ) 

  print ("Selecting Random Joke.")
 
  time.sleep (3)

  print (f"Random Joke is: {joke_selected}")  
# This is the inner while loop to enshure that the user enters a suported response 
  valid_input = False
  while valid_input == False: 
    keep_playing = input ("Would You Like To Keep Playing Yes/No")
  
    if keep_playing == "Yes" or keep_playing == "yes":
      valid_input = True
      continue
    elif keep_playing == "No" or keep_playing == "no":
      print ("Goodbye Thank You For Using Random Joke Generator Version 1.4 By JeffyGamez") #<--- Remember to change this lines version number when changing to one
      valid_input = True
      break
    else:
      print ("ERROR, Invalid Input!")
      
  



