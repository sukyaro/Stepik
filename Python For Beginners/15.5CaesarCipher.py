
# This code applies a Caesar cipher to each word in the input. 
# The shift for each word is equal to the number of letters (ignoring punctuation) in that word.
# Punctuation and non-letter characters remain unchanged, and letter case is preserved.
def coding_en(text, shift):
    code = ""
    for i in text:
        if i in ',. !-?"':
            code += i
        else:
            if i == i.upper():
                i = i.lower()
                if ord(i) + shift > 122:
                    code_1 = ord(i) + shift - 122 + 96
                else:    
                    code_1 = ord(i) + shift
                code += chr(code_1).upper()
            else:
                if ord(i) + shift > 122:
                    code_1 = ord(i) + shift - 122 + 96
                else:    
                    code_1 = ord(i) + shift
                code += chr(code_1)
    return code

a = input().split()
for i in a:
    c = 0
    for j in i:
        if j in '",.?!-':
            c += 1
    b = len(i) - c
    print(coding_en(i, b), end=" ")
