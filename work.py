s = input("Введіть рядок: ")

suma = 0
dobutok = 1

for c in s:
    if c.isdigit():
        suma = suma + int(c)
        dobutok = dobutok * int(c)

print("Сума цифр =", suma)
print("Добуток цифр =", dobutok)