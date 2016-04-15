import xmlrpclib
import sys

def conectarConOdoo():
    server = "localhost"
    port = 8069
    return xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'db'))

def crearNuevaBase(conexion):
    if len(sys.argv) != 2 :
        raise StandardError("Falta el nombre o has pasado algo de mas")

    nombre = sys.argv[1]
    if conexion.db_exist(nombre):
        raise StandardError("Esta base de datos ya existe")
    conexion.create_database('postgres', nombre, True, 'en_GB','admin')

def listarBases(conexion):
    print 'Listado de bases de datos:'
    l=conexion.list()
    for i in l:
        print i


conn = conectarConOdoo()
crearNuevaBase(conn)
listarBases(conn)
