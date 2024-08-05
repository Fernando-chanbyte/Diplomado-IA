num_sec = 2
adivinado = False

while not adivinado:
    num1 = int(input('introduce el primer numero '))
    if num_sec == num1:
        print('FELICIDADES')
        adivinado = True
    else:
        print('intenta de nuevo')