#Function to calculate factorial
def factorial(n):
    if n == 0 or n ==1:# base case: 0! and 1! are both 1
        return 1
    else:
        return n * factorial(n - 1)# recursive call
    
    #input from user
num = int(input("enter a number :"))

# check if the number is negative
if num < 0:
    print("factorial does not exist for negative numbers.")
else:
    print("the factorial of ",num,"is",factorial(num))
