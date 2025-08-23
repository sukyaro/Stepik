
# Question 1
# Count the number of positional arguments passed
def count_args(*args):
    return len(args)

# Question 2
# Return the sum of squares of all positional arguments
def sq_sum(*args):
    sum = 0
    for i in args:
        sum += i ** 2
    return sum

# Question 3
# Compute the mean of numeric positional arguments; ignore non-numeric
def mean(*args):
    sum, counter = 0, 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
            counter += 1
    if counter == 0:
        return 0
    return sum / counter

# Question 4
# Greet the first name and optionally other names
def greet(name, *args):
    return f"Hello, {name}" + (f" and {' and '.join(args)}!" if args else "!")

# Question 5
# Print a numbered list of non-empty string products or a message if none
def print_products(*args):
    shopping_bag = []
    for i in args:
        if type(i) == str and i != "":
            shopping_bag.append(i)
    if len(shopping_bag) == 0:
        print("Нет продуктов")
        return
    for i in range(len(shopping_bag)):
        print(f"{i + 1}) {shopping_bag[i]}")

# Question 6
# Print sorted key-value pairs from keyword arguments
def info_kwargs(**kwargs):
    data = (sorted(kwargs.items()))
    for i in data:
        print(f"{i[0]}: {i[1]}")
