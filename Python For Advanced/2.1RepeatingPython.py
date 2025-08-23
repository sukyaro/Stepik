# Part 1
# Question 1: 
# Reads two integers and prints their sum, difference, product, division, floor division, remainder, and sqrt(a^10 + b^10).
a, b = int(input()), int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a ** 10 + b ** 10) ** 0.5)

# Question 2: 
# Calculates BMI and prints weight category.
def if_norm(mass, height):
    return mass / (height * height)

imt = if_norm(float(input()), float(input()))
if imt < 18.5:
    print("Low weight")
elif 18.5 <= imt <= 25:
    print("Optimal weight")
else:
    print("High weight")

# Question 3: 
# Calculates cost (£x yp) based on length of input string (each character = 60p).
a, b = input(), 0
for i in a:
    b += 60
print(f"£{b // 100} {b % 100}p.")

# Question 4: 
# Counts number of words in input string.
print(len(input().split()))

# Question 5: 
# Determines Chinese zodiac animal for given year.
year = int(input())
ans = (year - 2000) % 12
if ans == 0:
    print("Dragon")
elif ans == 1:
    print("Snake")
elif ans == 2:
    print("Horse")
elif ans == 3:
    print("Sheep")
elif ans == 4:
    print("Monkey")
elif ans == 5:
    print("Chicken")
elif ans == 6:
    print("Dog")
elif ans == 7:
    print("Pig")
elif ans == 8:
    print("Rat")
elif ans == 9:
    print("Bull")
elif ans == 10:
    print("Tiger")
else:
    print("Rabbit")

# Question 6: 
# Reverses digits of input number and removes leading zeros.
num = [" ".join(i) for i in input()]
if len(num) == 5:
    num_1 = ""
    num.reverse()
    num = "".join(num)
    for i in num:
        if num.startswith("0"):
            num = num [1:]
            continue
        else:
            num_1 += i
    print(num_1)
else:
    print(num[0], end="")
    print(*num[-1:0:-1], sep="")

# Question 7: 
# Formats a number with commas every 3 digits from the right.
num = [i for i in input()]
for i in range(len(num) - 3, 0, -3):
    num.insert(i, ",")
print(*num, sep="")

# Question 8: 
# Josephus problem – eliminates every k-th person until one remains.
n = [x for x in range(1, int(input()) + 1)]
k, c_i = int(input()), 0

while len(n) > 1:
    c_i = (c_i + k - 1) % len(n)
    del n[c_i]

print(n[0])


# Part 2
# Question 1: 
# Counts number of points in each quadrant from given coordinates.
a, b = int(input()), []
for i in range(a):
    b.append([int(x) for x in input().split()])

first, second, thirs, fourth = 0, 0, 0, 0
for i in range(len(b)):
    x, y = 0, 0
    for j in b[i]:
        if j != 0:
            if b[i][0] > 0:
                x += 0.5
            else:
                x -= 0.5
            if b[i][1] > 0:
                y += 0.5
            else:
                y -= 0.5
            if x == 1 and y == 1:
                first += 1
            elif x == 1 and y == -1:
                fourth += 1
            elif x == -1 and y == 1:
                second += 1
            elif x == -1 and y == -1:
                thirs += 1
        else:
            continue

print(f"Fisrt quater: {first}")
print(f"Second quater: {second}")
print(f"Third quater: {thirs}")
print(f"Fourth quater: {fourth}")

# Question 2: 
# Counts how many times an element is greater than the previous one.
a = [int(x) for x in input().split()]
counter = 0
temp = a[0]
for i in range(1, len(a)):
    if a[i] > temp:
        counter += 1
    temp = a[i]

print(counter)

# Question 3: 
# Swaps every pair of adjacent elements in a list.
a, c = [int(x) for x in input().split()], []
if len(a) % 2 != 0:
    b = len(a) - 1
else:
    b = len(a)
    
for i in range(0, b, 2):
    c.append(a[i + 1])
    c.append(a[i])

if len(a) % 2 != 0:
    c.append(a[-1])

print(*c)

# Question 4: 
# Cyclically shifts list one step to the right.
a = [int(x) for x in input().split()]
a.insert(0, a[-1])
a.pop()
print(*a)

# Question 5: Counts number of distinct elements in a list.
a, b, counter = [int(x) for x in input().split()], [], 0
for i in a:
    if i not in b:
        b.append(i)
        counter += 1

print(counter)

# Question 6: 
# Checks if any two numbers in a list multiply to given value.
num_of_nums, nums, count = int(input()), [], 0
for i in range(num_of_nums):
    nums.append(int(input()))
mult = int(input())

for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        else:
            if nums[i] * nums[j] == mult:
                count += 1
                break

if count > 0:
    print("YES")
else:
    print("NO")

# Question 7: 
# Rock-paper-scissors game between Timur and Ruslan.
def play(a, b):
    if a == b:
        return "tie"
    elif a == "rock" and b != "paper":
        return "Timur"
    elif a == "scissors" and b != "rock":
        return "Timur"
    elif a == "paper" and b != "scissors":
        return "Timur"
    else:
        return "Ruslan"

print(play(input(), input()))

# Question 8: 
# Finds longest consecutive run of 'H' in input string.
line, counter_1, counter_2 = input(), 0, 0
for i in line:
    if i == "H":
        counter_1 += 1
    elif i == "T":
        if counter_1 > counter_2:
            counter_2 = counter_1
        counter_1 = 0

if counter_2 > counter_1:
    print(counter_2)
else:
    print(counter_1)

# Question 9: 
# Finds fridge numbers containing the subsequence "anton".
num_of_fridges, fridges, num = int(input()), [], []
for i in range(num_of_fridges):
    fridges.append(input())

for i in range(len(fridges)):
    counter = 0
    name = ["a", "n", "t", "o", "n", ""]
    for j in fridges[i]:
        if j == name[0]:
            counter += 1
            name.remove(j)
    
    if counter == 5:
        num.append(int(i) + 1)

print(*num, sep=" ")
