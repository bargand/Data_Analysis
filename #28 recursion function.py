def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))

#or

factorial_number = 3

num = 1

for i in range(1,factorial_number+1):
    num = num*i

print(num)