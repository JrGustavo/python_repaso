def add(*args):
    total = 0

    for number in args:
        total += number

    return total

res1 = add(1, 2, 3, 4, 5)
res2 = add(10, 20, 30, 40, 50)

print(f"Resultado {res1} ")
print(f"Resultado {res2} ")