def diamond(n):
    i = 0
    espaco = n // 2
    if n % 2 == 0 or n <= 0:
        return print("Não é possível realizar um diamante com valores pares.")

    else:
        while i <= n:
            if i % 2 == 0:
                i += 1
            else:
                print(espaco * " " + i * "*" + "")
                if i == n:
                    espaco = 1
                    i -= 1
                    while i >= 0:
                        if i % 2 == 0:
                            i -= 1
                        else:
                            print(espaco * " " + i * "*" + "")
                            i -= 1
                            espaco += 1
                    i = n + 1
                i += 1
                espaco -= 1

diamond(0) # Insira um valor ímpar para receber um diamante que corresponda a este valor