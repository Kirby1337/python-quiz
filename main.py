# Create a Quiz

# Input

answerOne = 'ottawa'
answerTwo = 'asia'
answerThree = 'justin trudeau'
answerThree2 = 'trudeau'
answerFour =  'joe biden'
answerFour2 = 'biden'
score = 0

#Process 

questionOne = (input("What is the capital of Canada: "))
if answerOne in questionOne:
  print("You got the answer correctly!")
  score+=1
else:
    print("Your answer is wrong, it is Ottawa.")

questionTwo = (input("What is the largest continent: "))
if answerTwo in questionTwo:
  print("You got the answer correctly!")
  score+=1
else:
  print("Your answer is wrong, it is Asia.")

questionThree = (input("Who is the Prime Minister of Canada: "))
if answerThree.lower() in questionThree.lower():
  print("You got the answer correctly!")
  score+=1
elif answerThree2.lower() in questionThree.lower():
  print("You got the answer correctly!")
  score+=1
else:
  print("Your answer is wrong, it is Justin Trudeau")

questionFour = (input("Who is the current president of the USA: "))
if answerFour in questionFour:
  print("You got the answer correctly!")  
  score+=1
elif answerFour2.lower() in questionFour.lower():
  print("You got the answer correctly!")
  score+=1
else:
  print("Your answer is wrong, it is Joe Biden.")
print('You have completed the quiz!')



# Answer Output
averageScore = int((score/4 * 100))
total = 4

if score == 4:
  print("You did amazing and got a perfect score!", score, "/", total, averageScore, "%")
elif score == 3:
  print("Aw, close score to getting a perfect, but still good job!", score, "/", total, averageScore, "%")
elif score == 2:
  print("You got half of the quiz correctly, good job.%", score, "/", total, averageScore, "%")
elif score == 1:
  print("Nice try, but you need to work a little bit harder.", score, "/", total, averageScore, "%")
elif score == 0:
  print("You got all the answers wrong, you might need to review.", score, "/", total, averageScore, "%")

