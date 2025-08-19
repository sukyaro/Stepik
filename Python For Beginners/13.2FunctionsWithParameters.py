
# Question 1
# Draw a diamond-like triangle pattern with a given character and base size
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 1):
        print(fill * i)
    for i in range(base // 2 + 1, 0, -1):
        print(fill * i)

draw_triangle(input(), int(input()))

# Question 2
# Print the initials of a person in uppercase
def print_fio(name, surname, patronymic):
    a = (surname[0] + name[0] + patronymic[0]).upper()
    print(a)

print_fio(input(), input(), input())

# Question 3
# Calculate and print the sum of digits of a number
def print_digit_sum(num):
    sum = 0
    while num > 0:
        l_d = num % 10
        sum += l_d
        num //= 10
    print(sum)

print_digit_sum(int(input()))
