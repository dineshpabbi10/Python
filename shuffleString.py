import random
from collections import Counter
from math import factorial
def shuffle(data):
    data2 = list()
    un =  list()
    length = len(data)
    while(len(data2) != length):
        x = random.randint(0,length-1)
        check = (x in un)
        if(not check):
            un.append(x)
            data2.append(data[x])
    return data2
def randString(data):
    strings = list()
    strings.append(''.join(data))
    while(len(strings) != count("".join(data))):
        x = ''.join(shuffle(data))
        if(not(str(x) in strings)):
            strings.append((str(x)))
    for i in strings:
        print(i)
def count(s):
    """Return the number of different permutations of s."""
    s = str(s)
    c = 1
    for i in Counter(s).values():
        c *= factorial(i)
    return factorial(len(s)) // c
def randomizer():
    y = input("Enter a string to randomize\n")
    y = list(y)
    randString(y)
randomizer()


