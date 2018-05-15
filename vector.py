class vector:
    """Initialize Vector"""
    def __init__(self,d):
        self.coords = [0]*d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, item): #Getting an item from a vector
        return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value

    def __add__(self, other):
        if(len(self)!= len(other)):
            print("Don't add these too ! they are not same types :P")
        else:
            result = vector(len(self))
            for i in range(0,len(result)):
                result[i] = self[i] + other[i]
            return result
    def __sub__(self, other):
        if(len(self) != len(other)):
            print("Dont subtract these two!")
        else:
            result = vector(len(self))
            for i in range(0,len(result)):
                result[i] = self[i] - other[i]
            return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return self.coords != other.coords

    def __str__(self):
        return '<'+ str(self.coords)[1:-1] +'>'

print("Input for vector 1")
x = vector(2)
for i in range(0,len(x)):
    x[i] = int(input('Enter a number\n'))
print("Input for vector 2")
y = vector(2)
for i in range(0,len(y)):
    y[i] = int(input('Enter a number\n'))

z = x-y
print(str(x))
print("  +  ")
print(str(y))
print("  =  ")
print(str(z))
