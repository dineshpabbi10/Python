import random
# x = random.randint(5,10)
# print(x)
data = [1,2,3,4,5,10]

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

    print(data2)

shuffle(data)