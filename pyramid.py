#!usr/env python3

for j in range(9):
  if(j >= 5):
    step = -1
  else:
    step = 1
  for i in range(j+1,5,step):
    print("*", end="")
