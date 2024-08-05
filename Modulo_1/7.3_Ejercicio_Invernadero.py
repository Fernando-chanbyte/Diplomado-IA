
# inicializar el contador

contador = 0

while contador < 3:
    temperatura = float(input('ingrese la temperatura: '))

    humedad = float(input('ingrese la humedad: '))

    if temperatura > 30:
        if humedad >= 30:
            accion = 'se recomienda ventilacion'
        else: 
            accion = 'se recomienda riego y ventilacion'
    else:
        if humedad < 30:
            accion = 'se recomienda riego'
        else:
            accion = 'sin acciones'

    print(accion)

    contador += 1