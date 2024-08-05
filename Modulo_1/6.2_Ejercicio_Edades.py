def check_age(age):
    if age < 13:
        return 'niño'
    elif age < 18:
        return 'adolescente'
    elif age < 65:
        return 'adulto'
    else:
        return 'adulto mayor'
    
age = int(input('ingresa su edad: '))

if (type(age) == int) and (age >= 0):
    print(f'su edad: {age}, corresponde a {check_age(age)}')
else:
    print('ingrese su edad en numeros naturales')