import time 
import random
print ("This repo was made by jeffygamez")
print ("now loading")
time.sleep (5)
print ("Welcome To Random Joke Generator version 1.2.7")
joke_1 = "Why did the chicken cross the road? To run from the KFC"
joke_2 = "Have you heard the rummor of the margerin? Never mind I butter not spread it"
joke_3 = "What did the eraser say to the pencil? You're look'n mighty sharp today"

joke_selected = random.randin (1, 3) 

print (f"Selecting Random Joke Number: {joke_selected}")

time.sleep (3)

if joke_selected == 1:
  print (f"Random Joke Is: {joke_1}")

if joke_selected == 2:
  print (f"Random Joke Is: {joke_2}")

if joke_selected == 3:
  print (f"Random Joke Is: {joke_3}")
