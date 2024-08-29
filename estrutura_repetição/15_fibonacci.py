n = int(input("Digite um número: "))

# Os dois primeiros números da sequência
a, b = 1, 1

if n <= 0:
    print("Por favor, digite um número maior que 0.")
else:
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2, n):
        f = a + b
        print(f)
        a = b
        b = f
