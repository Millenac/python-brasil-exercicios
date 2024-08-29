a, b = 1, 1

print(a)
print(b)

while True:

    f = a + b
    if f > 500:
        break

    print(f)
    a = b
    b = f