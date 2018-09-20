n = int(input("Enter the size of square matrix"))
l = list()
final = list()
for i in range(n):
	for j in range(n):
		x = int(input())
		l.append(x)
	final.append(l)
	l = list()
	

for i in range(n):
	for j in range(n):
		print(final[i][j],end=" ")
	print()


up = 0
down = n-1
left = 0
right = n-1

while left<right and up<down :
	temp1 = final[up][right]
	for i in range(right,left,-1):
		final[up][i] = final[up][i-1]

	temp2 = final[down][right]
	for i in range(down,up+1,-1):
		final[i][right] = final[i-1][right]

	final[up+1][right] = temp1

	temp1 = final[down][left]
	for i in range(left,right-1):
		final[down][i] = final[down][i+1]

	final[down][right-1] = temp2

	for i in range(up,down-1):
		final[i][left] = final[i+1][left]

	final[down-1][left] = temp1

	up += 1
	down-= 1
	left+=1
	right-=1


print("Rotated Matrix is")
for i in range(n):
	for j in range(n):
		print(final[i][j],end=" ")
	print()



