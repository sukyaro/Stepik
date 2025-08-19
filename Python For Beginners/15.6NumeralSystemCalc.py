
# This code reads an integer and prints its representation in binary, octal, and hexadecimal.
# The binary and octal outputs remove the '0b' and '0o' prefixes.
# The hexadecimal output is in uppercase and removes the '0x' prefix.
num = int(input())
print(bin(num)[2:])
print(oct(num)[2:])
print(hex(num)[2:].upper())