#from random import randint
import random


# Using Sattolo's algorithm (variation of Fisher-Yates) for a complete random shuffle 
def sattolo(a):
    size = len(a)
    for i in range(size-1):
        j = random.randrange(i+1, size)
        a[i], a[j] = a[j], a[i]
    # print(a)
    return a

def santa(a, b):
    for x in range(len(a)):
        print(f"{b[x]} is buying for {a[x]}")


array = []
total = input("How many people will participate in the Secret Santa? ")
for x in range(int(total)):
    participant = input("Who will participate in the Secret Santa? ")
    array.append(participant)

# array = ["Aris", "Ikenna", "Julliene", "Samrawi", "Philip", "Rey"]
fordapeople = array.copy()

sattolo(array)

santa(array, fordapeople)

# fordapeople.append("Radek")

