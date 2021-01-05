#!/usr/bin/env python3
from random import randint

def askQuestion(index):
  questionOrder = randint(0,1)
  query = " "
  result = -1
  if questionOrder:
    query = f"(A) Would you rather {questions[index][1]}\nor\n(B) Would you rather {questions[index][0]}\nA or B?"
    answer = input(query).strip().upper()
    if answer == "A":
      result = 1
    elif answer == "B":
      result = 0
    else:
      print("Not a valid selection.  A or B only.")
      result = askQuestion(index)
  else:
    query = f"(A) Would you rather {questions[index][0]}\nor\n(B) Would you rather {questions[index][1]}\nA or B?"
    answer = input(query).strip().upper()
    if answer == "B":
      result = 1
    elif answer == "A":
      result = 0
    else:
      print("Not a valid selection.  A or B only.")
      result = askQuestion(index)
  return result

questions = [["date the wealthiest person?", "date your celebrity crush?"],
  ["win a Harley motorcycle?", "win a BMW motorcycle?"],
  ["have more money?", "have more time?"],
  ["live without internet for a year?", "live without a phone for a year?"],
  ["be Thanos?", "be Captain Marvel?"]]

index = 0
count = 0
while index < len(questions):
  count += askQuestion(index)
  index += 1

if count >= len(questions)/2:
  print("You are a punk!!")
else:
  print("You are a princess!!")






