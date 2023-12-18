#An= An-2 + An-1
x = abs(int(input("Type any positive number:")))

n1, n2= 0,1
count = 0

while count < x :
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1



