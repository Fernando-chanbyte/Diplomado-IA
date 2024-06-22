"""
Escribir un programa que solicite dos números y luego imprima:
    1. La suma de los dos números
    2. La resta de primer número menos el segundo
    3. El producto de los dos números
    4. El cubo de la suma de los dos numeros
    5. El cociente de la división del primer número por el segundo
"""
num1 = float(input("ingrese el primer número: "))
num2 = float(input("ingrese el segundo número: "))

print("La suma de los dos números:", num1 + num2 )
print("La resta del primer número menos el segundo:", num1 - num2 )
print("El producto de los dos números:", num1 * num2 )
print("El cubo de la suma de los dos numeros:", (num1 + num2)**3 )
print("El cociente de la división del primer número por el segundo:", num1 / num2)
