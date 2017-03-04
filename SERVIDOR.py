# INICIO DEL PROGRAMA

import socket



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("", 35000))

server.listen(1)

socket_cliente, direccion = server.accept()

# tamano de los mensajes enviados por el cliente

while True:   # esperando conexion

    mensaje_cliente = socket_cliente.recv(1024)
    if mensaje_cliente == "lina":
        print "Usuario Correcto"
    else:
        print "usuario incorrecto"

    clave = socket_cliente.recv(1024)
    if clave == "1234":
        print "clave correta"
        print 'Bienvenida'

        import archivo
        archivo.archivos()
        archivo.escribir()
    else:
        print "clave incorrecta"


    salir = socket_cliente.recv(1024)
    if salir == "salir":
        break


print "Hasta Pronto"
socket_cliente.close()
server.close()




'''
print str(direccion[0]) + " escribio: ", mensaje_cliente
mensaje_servidor = raw_input("Ingrese Respuesta al Cliente >> ")
socket_cliente.send(mensaje_servidor)
'''
# imprimir la direccion ip del cliente str(addr[0])+

