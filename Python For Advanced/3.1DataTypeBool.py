
# Question 1
# Checks if the first number is divisible by the second and prints the result.
def func(num1, num2):
    return num1 % num2 == 0

if func(int(input()), int(input())):
    print("divisible")
else:
    print("not divisible")