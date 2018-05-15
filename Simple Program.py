def method():
    grades = {"A+" : 4,"A" : 3.4,"B+" : 3 ,"B" : 2.6,"C+" : 2,"C": 1.7,"D+": 1,"D":0}
    total = 0
    subjects = 0
    done = False
    num = int(input("Enter the number of subjects you studied this semester\n"))
    print("""Enter your Grades""")
    while num>0:
        grade = input()
        if grade == "end":
            done = True
        elif grade not in grades :
            print("The grade {0} is not a legal grade".format(grade),end=" Dinesh is best")
            subjects = 0
        else:
            subjects += 1
            total = total + grades[grade]
        num -= 1

    if subjects > 0  :
        print("Your average score is {0}".format(total/subjects))

method()