import random

list1 = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
file1 = open("valorantpointskey.txt", "w")
total1 = int(input("How much to create ? >> "))

print("Valorant Points keys are generated and saved in the valorantpointskey.txt file.")

def create():
  for x in range(total1):
    print("RA-" + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1),file = file1, flush = True)

create()