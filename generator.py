def factor(n):
    k = 1
    while (k*k < n):
        if(n%k == 0):
            yield k
        k += 1
    # z = k
    while (k*k >0):
        if(n%k == 0):
            yield n//k
        k -= 1
    # if(z*z == n):
    #     yield z

for x in factor(100):
    print(x)