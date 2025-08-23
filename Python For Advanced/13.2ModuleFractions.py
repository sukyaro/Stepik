
from fractions import Fraction
from math import *

# Question 1
# Convert each decimal string to a Fraction and print
numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
for i in numbers:
   frac_number = Fraction(i)
   print(i + " = " + str(frac_number))

# Question 2
# Find min and max of decimals as Fractions and print their sum
s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
new_list = s.split(" ")
print(Fraction(min(new_list)) + Fraction(max(new_list)))

# Question 3
# Convert two integers into a Fraction and print
num1 = int(input())
num2 = int(input())
print(Fraction(num1, num2))

# Question 4
# Perform arithmetic operations between two fractional inputs
num1 = input()
num2 = input()

print(num1 + " + " + num2 + " = " + str(Fraction(num1) + Fraction(num2)))
print(num1 + " - " + num2 + " = " + str(Fraction(num1) - Fraction(num2)))
print(num1 + " * " + num2 + " = " + str(Fraction(num1) * Fraction(num2)))
print(num1 + " / " + num2 + " = " + str(Fraction(num1) / Fraction(num2)))

# Question 5
# Sum the series 1/(i^2) for i from 1 to number as a Fraction
number = int(input())
fractional_number = 0
for i in range(1, number + 1):
   fractional_number += Fraction(1, i**2)

print(fractional_number)

# Question 6
# Sum the series 1/(i!) for i from 1 to number as a Fraction
number = int(input())
fractional_number = 0

for i in range(1, number + 1):
   fractional_number += Fraction(1, factorial(i))

print(fractional_number)

# Question 7
# Find the largest fraction i/j < 1 with i+j equal to a given number
number = int(input())
number2 = Fraction(0)

for i in range(1, number + 1):
   for j in range(1, number + 1):
       currNumber = Fraction(i, j)
       if (i < j) and (currNumber.numerator + currNumber.denominator == number) and (i > number2.numerator or j > number2.denominator):
           number2 = currNumber

print(number2)

# Question 8
# Generate all fractions i/j < 1 with i,j from 1 to number, sort and print
number = int(input())
setOfNums = set()

for i in range(1, number + 1):
    for j in range(1, number + 1):
        currNumber = Fraction(i, j)
        if currNumber < 1:
            setOfNums.add(currNumber)
            
print(*sorted(setOfNums), sep="\n")
