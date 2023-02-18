import re

print("Введите букву a")
a = input()
print("Введите букву b")
b = input()

with open('txt.txt') as f:
    s = f.read()


print(re.findall(r'\b[A-Za-z]{2}a[A-Za-z]*b[A-Za-z]{2}\b',s))
