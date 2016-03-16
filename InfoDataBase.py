import xmlrpclib
import sys

def conectarConOdoo():
    server = "localhost"
    port = 8069
    return xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'common'))

def obtenerInfoSobreBase(conexion):
    if len(sys.argv) != 4 :
        raise StandardError("Falta un argumento o has pasado algo de mas")
    nombre = sys.argv[1]
    usuario = sys.argv[2]
    password = sys.argv[3]

    print(conexion.version())
    print(conexion.about())
    print(conexion.timezone_get(nombre, usuario, password))

conn = conectarConOdoo()
obtenerInfoSobreBase(conn)