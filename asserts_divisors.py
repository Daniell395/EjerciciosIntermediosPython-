def divisors(num):
    divisors =[]
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run(): 
    num = input('Escribe un numero para sacar sus divisores: ')

    if num.isnumeric():
        print(divisors(int(num)))

    else:
        try:
            num = int(num)
        except:
            return print("No debes ingresar letras o caracteres")
    
        
        assert num > 0, "Debes ingresar un numero positivo"
        

if __name__ == '__main__':
    run()