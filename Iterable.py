data = [1,2,3,4]
i = iter(data)
while True:
    try:
        print(next(i))
    except StopIteration:
        break
