
def factorial(n):
    if (n == 0) or n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        return res


print(f"Resultado: {factorial(5)}")


def fibonnacci(number: int) -> int:
    if number <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonnacci(number - 1) + fibonnacci(number - 2)


print(fibonnacci(5))
