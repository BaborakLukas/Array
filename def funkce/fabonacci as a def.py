# def fibonacci_of(n):
#     if n in {0, 1}:  
#         return n
#     return fibonacci_of(n - 1) + fibonacci_of(n - 2) 


# print(fibonacci_of(5))


#An= An-2 + An-1
def fibonaci(a,b,c):

    x=0

    fib = [0]

    while x<=c:

         fib.append(b)

         a,b = b , a+b

         x+=1

    return fib

print(fibonaci(0,1,100))