def divisors(num):
    try:
        if num < 0:
            raise ValueError('Ingresa solo números positivos')
        else:
            divisors = [i for i in range(1, num + 1) if num % i == 0]
            return divisors
    except ValueError as value_error:
        print(value_error)
        return str(num) + " No es nu numero positivo"


def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")


if __name__ == "__main__":
    run()