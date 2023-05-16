import string
import random 
import time   

response = "a"              # the variable that will hold the user's response
c = "b"                     #the variable that will hold the character the user should type
score = 0                   #the variable that will hold the user's score
start = time.time()         #the variable that holds the starting time
elapsed = 0                 #the variable that holds the number of seconds elapsed.
while elapsed < 30:         #while less than 30 seconds have elapsed  

    if response == c:       #if the response from the previous loop matches the character
        score += 1          #from the previous loop, increase the score.

    #c is a random character
    c = random.choice(string.ascii_lowercase + string.digits)
    print(c)               

    response = input("Type a letter or a number: ") #get the user's response

    elapsed = time.time() - start #update the time elapsed