fib_set = {0, 1}
x, y = 0, 1

while True:
    n = int(input("Insira um numero: "))

    try:
        number = int(n)
    except ValueError:
        print("Por favor, insira um numero inteiro")
        continue

    if number < 0:
        print("Por favor, insira um numero positivo")
        continue

    if number in fib_set:
        print("O numero pertence a sequencia de Fibonacci")
    else:
        while y <= number:
            x, y = y, x + y
            fib_set.add(y)
            if y == number:
                print("O numero pertence a sequencia de Fibonacci")
                break
        else:
            print("O numero nao pertence a sequencia de Fibonacci")
