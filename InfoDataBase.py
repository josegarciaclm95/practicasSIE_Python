import xmlrpclib
import sys

def conectarConOdoo():
    server = "localhost"
    port = 8069
    return xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'common'))

def obtenerInfoSobreBase(conexion):
    if len(sys.argv) != 2 :
        raise StandardError("Falta uno nombre o has pasado algo de mas")
    nombre = sys.argv[1]
    print(conexion.version())
    print(conexion.about())
    print(conexion.timezone_get(nombre, 'admin', 'admin'))

conn = conectarConOdoo()
obtenerInfoSobreBase(conn)