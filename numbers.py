#Given a sequence of positive integers. Determine how many times the largest of them is among the given numbers.
#if the input is an array of elements [23,3,14,11,25,65,8,3,65,0], then the output will be the largest number = 65 and their number in the array = 2

numbers = [23,3,14,11,25,65,8,3,65,0]

max = 0 
times = 0

for x in numbers: 
    if(max<x):
        max = x 
        times = 0
    if(max == x):
         times += 1 


print("The largest number is:",max,"and its there",times,"times")
