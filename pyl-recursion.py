# factorial(7) = 7*6*5*4*3*2*1
#factorial(6) = 6*5*4*3*2*1
#factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
#factorial(0) = 1

# factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
    return 1
else:
    return  n * factorial(n-1)

print(factorial(5))
# 5* factorial(4)
# 5 * 4 factorial(3)
# 5 * 4 * 3 factorial(2)
# 5 * 4 * 3 * 2 factorial(1)
# 5 * 4 * 3 * 2 * 1

#f0 = 0
#f1 = 1
#f2 = f(1)+ f(0)
# fn = f (n - 1) + f(n - 2)
