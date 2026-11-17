#from random import randint
import random

fordapeople = None

# Using Sattolo's algorithm (variation of Fisher-Yates) for a complete random shuffle 
def sattolo(a):
    size = len(a)
    fordapeople = array
    for i in range(size-1):
        j = random.randrange(i+1, size)
        a[i], a[j] = fordapeople[j], fordapeople[i]
    print(fordapeople)


array = [1,2,3,4,5,6,7,8,9,10]
sattolo(array)

