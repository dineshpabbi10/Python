class stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.data[-1]

    def push(self,x):
        self.data.append(x)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.data.pop()

    def display(self):
        print(self.data)


def infix_to_postfix(x):
    s = stack()
    result = ""
    p = {"^":3,"*":2,"/":2,"+":1,"-":1}
    for i in x:
        try:
            if i in "^*/+-":

                if(s.top() == "("):
                    s.push(i)
                elif (p[i]>=p[s.top()]):
                    s.push(i)
                else:
                    while(p[i]<=p[s.top()]):
                        result+=s.pop()
                    s.push(i)


            elif i == "(":
                s.push(i)
            elif i == ")":
                while s.top() != "(":
                    result+= s.pop()
                s.pop()
            else:
                result+=i
        except Exception:
            s.push(i)
        # print(s.display())
    while not(s.is_empty()):
        result+=s.pop()
    return result

y = input("Enter the expression\n")
print("Postfix notation is")
ans = infix_to_postfix(y)
print(ans)



####  Evaluation of postfix notation
def evaluate(ans):
    s = stack()
    for i in ans:
        if(i in "+-*/^"):
            temp1 = float(s.pop())
            temp2 = float(s.pop())
            if i == "+":
                s.push(temp1+temp2)
            elif i == "-":
                s.push(temp2-temp1)
            elif i == "*":
                s.push(temp1*temp2)
            elif i == "/":
                s.push(temp2/temp1)
            else:
                s.push(temp2^temp2)
        else:
            s.push(i)
    print(s.pop())

evaluate(ans)
