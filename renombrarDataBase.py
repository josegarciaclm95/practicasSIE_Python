import xmlrpclib
import sys

def conectarConOdoo():
    server = "localhost"
    port = 8069
    return xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'db'))

def renombrarBase(conexion):
    if len(sys.argv) != 3 :
        raise StandardError("Falta uno o dos nombres o has pasado algo de mas")
    actual = sys.argv[1]
    futuro = sys.argv[2]
    if not conexion.db_exist(actual):
        raise StandardError("La base de datos %s no existe" % (actual))
    if conexion.db_exist(futuro):
        raise StandardError("La base de datos %s ya existe" % (futuro))
    conexion.rename('postgres', actual, futuro)

def listarBases(conexion):
    print 'Listado de bases de datos:'
    l=conexion.list()
    for i in l:
        print i


conn = conectarConOdoo()
renombrarBase(conn)
listarBases(conn)
