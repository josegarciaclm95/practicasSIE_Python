import xmlrpclib
import sys

def conectarConOdoo():
    server = "localhost"
    port = 8069
    return xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'db'))

def eliminarBase(conexion):
    if len(sys.argv) != 2 :
        raise StandardError("Falta uno nombre o has pasado algo de mas")
    nombre = sys.argv[1]
    if not conexion.db_exist(nombre):
        raise StandardError("La base de datos {0} no existe".format(nombre))
    confirmacion = raw_input("Esta seguro de que desea eliminar esta base de datos? S/N \n")
    if confirmacion in ('S'):
        conexion.drop('postgres',nombre)

def listarBases(conexion):
    print 'Listado de bases de datos:'
    l=conexion.list()
    for i in l:
        print i


conn = conectarConOdoo()
eliminarBase(conn)
listarBases(conn)
