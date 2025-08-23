from decimal import *

# Question 1
# Convert strings to Decimal and find the sum of min and max values
s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
newList = [Decimal(i) for i in s.split(" ")]
print(max(newList) + min(newList))

# Question 2
# Sort decimals descending, print total sum, and first 5 largest numbers
s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
newList = [Decimal(i) for i in s.split(" ")]
newList.sort(reverse=True)
print(sum(newList))
print(" ".join([str(newList[x]) for x in range(5)]))

# Question 3
# Sum the min and max digits of the decimal number
number = Decimal(input())
number_1 = int(number)
if number_1 == 0:
   print(0 + max(Decimal.as_tuple(number).digits))
else:
   print(min(Decimal.as_tuple(number).digits) + max(Decimal.as_tuple(number).digits))

# Question 4
# Calculate exp, ln, log10, and sqrt of a decimal number and sum them
d = Decimal(input())
print(Decimal.exp(d) + Decimal.ln(d) + Decimal.log10(d) + Decimal.sqrt(d))
