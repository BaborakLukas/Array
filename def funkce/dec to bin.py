x = int(input("Input number:"))
y = 0
numbers = []
while x > 0: 
    y = x // 2
    if x % 2 != 0:
        numbers.append(1)
    else:
        numbers.append(0)
    x = y 

numbers = reversed(numbers)
print(*numbers)









# napsat z bin do dec a dec do bin