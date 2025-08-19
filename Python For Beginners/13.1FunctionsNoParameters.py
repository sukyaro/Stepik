
# Question 1
# Draw a rectangle box with '*' characters
def draw_box():
    print("*" * 10)               # Top border
    for i in range(12):           # Middle rows
        print("*" + " " * 8 + "*")
    print("*" * 10)               # Bottom border

draw_box()

# Question 2
# Draw a right-angled triangle with '*' characters
def draw_triangle():
    for i in range(1, 11):       # Rows 1 to 10
        print("*" * i)

draw_triangle()
