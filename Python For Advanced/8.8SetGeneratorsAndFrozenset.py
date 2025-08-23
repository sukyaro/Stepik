
# Question 1
# Converts all items to integers, removes duplicates, and prints them sorted.
items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
myset = {int(i) for i in items}
print(*sorted(myset))


# Question 2
# Collects the first letters of all words in lowercase and prints them sorted.
words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
myset = {i.lower()[:1] for i in words}
print(*sorted(myset))


# Question 3
# Extracts all unique words from the sentence, ignoring punctuation and case, then prints them sorted.
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
myset = {i.strip(':,.!?();').lower() for i in sentence.split()}
print(*sorted(myset))


# Question 4
# Extracts all unique words shorter than 4 letters, ignoring punctuation and case, then prints them sorted.
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
myset = {i.strip(':,.!?();').lower() for i in sentence.split() if len(i.strip(':,.!?();')) < 4}
print(*sorted(myset))


# Question 5
# Collects all filenames ending with ".png" (case-insensitive), converts them to lowercase, and prints them sorted.
files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
myset = {i.lower() for i in files if i[-4:].lower() == ".png"}
print(*sorted(myset))

