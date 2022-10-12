from datetime import datetime
from random import *
from math import sqrt

# Random para elijir a un conductor cuando hay mas de uno
# sino elige el disponible

def movildisponible():
    ran = randrange(len(lista))
    movilasignado = lista[ran]
    return movilasignado

# Ingreso de los datos del conductor y auto
def datos_auto():
    patente = input ("Ingrese patente de vehiculo a registrar:", )
    marca = input("ingrese marca:",  )
    modelo = input("Ingrese modelo de vehiculo:", )
    color = input('ingrese color del vehiculo:',)
    conductor = input("Ingrese nombre y apellido:", )
    telefono1 = input("Ingrese  numero telefonico movil:", )
#registro
    usuarion = {"patente": patente, "marca": marca, "modelo": modelo, "color": color, "conductor": conductor, "telefono": telefono1}
    lista.append(usuarion)
    return lista


# ingreso datos del pasajero
def datos_pasajero():
    telefono2 = input ("Ingrese telefono movil:", )
    nombre = input("ingrese nombre y apellido:",  )

#pasajero
    pasajero = {"telefono": telefono2, "nombre": nombre}
    usuario.append(pasajero)
    return usuario


# Calculo Viaje segun coordenadas
def calculo_viaje():
    precio_km = 350
    x1 = float(input('GPS Latitud: '))
    y1 = float(input('GPS Longitud: '))
    print('Ingresar datos de destino')
    x2 = float(input('GPS Latitud: '))
    y2 = float(input('GPS Longitud: '))
    distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
    precio_total = distancia * precio_km
    km = round(distancia)
    pt = round(precio_total)
    return km, pt


# LISTAS VACIAS
lista = []
usuario= []

# MOVIMIENTO AUTO
velocimetro = 0
# FECHA TIEMPO
now = datetime.now()

# PROGRAMA PRINCIPAL
opcion = 0
while opcion != 5:

# EL MENU PRINCIPAL
        print('\n** Bienvenidos a nuestra aplicación de viajes, por favor ingresa la opción de su elección **')
        print('\n== Menu Principal ==')
        print('1)-Para registrarte como conductor.')
        print('2)-Para registrarte como pasajero')
        print('3)-Para iniciar el viaje..')
        print('4)-Acelerar - Frenar - Detener')
        print('5)-Salir')

        if opcion < 0 or opcion > 5:
            print('\nIngresar opcion entre 1 y 6\n')
        if opcion == 1:
            conductor = datos_auto()
            print('Se ha agregado su registro como conductor:')
        if opcion == 2:
            pasajero = datos_pasajero()
            print('Se ha agregado su registro como usuario:')
        if opcion == 3:
            print('Esta seguro de Solicitar Viaje ?')
            respuesta = input('Ingresar SI o NO :').upper()
            while respuesta != 'SI' and respuesta != 'NO':
                print('Dato Invalido¡¡')
                respuesta = input('Ingresar SI o NO :').upper()
            if respuesta == 'SI':
                cal = calculo_viaje()
                print('='*26)
                print('Total Kilometros =', cal[0])
                print('Total Servicio =$', cal[1])
                print('='*26)
                tiempoespera = randint(1, 10)
                print('Tu Movil llegara en aprox.',
                    tiempoespera, 'minutos a recogerte')
                print('==Datos del Movil==')
                print('Fecha', now)
                ranmovil = movildisponible()
                print('Fecha', now)
                for x, y in ranmovil.items():
                    print('{:<10}: {}'.format(x, y))
                print('='*26)
        if opcion == 4:
            print('Acelerar = S')
            print('Frenar = F')
            print('salir = N')
            velocidad = input('desea acelerar? marque S para sí, y N para no:')
            while velocidad !='N' and velocidad != 'n':
                if velocidad == 'S' or velocidad == 's':
                    velocimetro += 10
                    print('Su Velocidad actual es ', velocimetro, 'KM/hr.')
                if velocidad == 'F' or velocidad == 'f':
                    velocimetro -= 10
                    print('Su Velocidad actual es ', velocimetro, 'KM/hr.')
                    if velocimetro == 0:
                        print('Auto detenido')
                velocidad = input('desea acelerar? marque S para sí, y N para no:')

        try:
            opcion = int(input('\nIngresar Opcion :'))
        except:
            print('!! Dato Invalido :( ¡¡')
print('==Gracias por usar nuestro servicio, te esperamos la proxima vez==')
