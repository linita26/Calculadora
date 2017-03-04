# INICIO DEL PROGRAMA

import socket

cliente = socket.socket()

"""direccion ip del servidor, puerto del servidor"""

cliente.connect(("localhost", 35000))

while True:

    mensaje_cliente = raw_input("ingrese su nombre: ")
    cliente.send(mensaje_cliente)

    clave = raw_input("ingrese su contrasena: ")
    cliente.send(clave)

    if (mensaje_cliente == 'lina' and clave == '1234'):
        print "CALCULAD0RA"

    else:
        print'No puede Acceder'
        break

    lista = ['1.suma', '2.Resta', '3.Multiplicacion', '4.Division', '5.salir']

    for i in lista:
            print i

   # opcion=raw_input('Ingrese la operacion a Realizar')
    #cliente.send(opcion)

    import operaciones

    operaciones.suma()
    operaciones.resta()
    operaciones.producto()
    operaciones.division()



    if mensaje_cliente == "salir":

        break



print "vuelva cuando quiera"
cliente.close()
















