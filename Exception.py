try:
    x = [1, 2, 3, 4, 5]
    x[7] = 10
except IndexError:
    print('Dont try buffer overflow attack in Python!')
