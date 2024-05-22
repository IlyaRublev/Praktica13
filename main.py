import string
with open("text.txt", "r") as file:
    a = file.read().lower()
for char in string.punctuation:
    a = a.replace(char, " ")
b = a.split()
c = {}
for d in b:
    if d in c:
        c[d] += 1
    else:
        c[d] = 1
for d, e in c.items():
    print(f"Слово '{d}' встречается {e} раз(а)в тексте.")