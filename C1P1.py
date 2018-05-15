"""TO check for multiplicity"""


def multicheck(a, b):
    if (a % b == 0):
        return True


print(multicheck(4, 2))

"""To check for Max and minimum number"""

# def maxmin(a):
#     x = a[0]
#     y = a[0]
#     for i in a:
#         if(i>x):
#             x = i
#
#         if(i<y):
#             y=i
#
#     return x,y
#
# m = [1,2,3,4,5,6,2,11]
# n = maxmin(m)
# print(n)

def sq():
    s = int(input("Enter the number\n"))
    y = list()
    for i in range(1,s):
        if(not(i % 2 == 0)):
            y.append(i*i)
    return y

print(sq())
