def vowels(x):
    count = 0
    for i in x:
        if(i =='a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'U' or i == 'u'):
            count += 1
    print("Number of Vowels in the string %s is %s"%(x,count))

vowels("AeiIx")