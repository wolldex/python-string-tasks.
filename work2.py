import random

n = int(input("Скільки рядків? "))

for i in range(n):
    s = input("Введіть рядок: ")
    d = len(s) // 3
    a = [s[:d], s[d:2*d], s[2*d:]]
    random.shuffle(a)

    print(a[0])
    print(a[1])
    print(a[2])