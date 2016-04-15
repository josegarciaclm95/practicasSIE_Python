#!/usr/bin/python
# coding: utf-8
#
# listar DBs

import xmlrpclib
import sys

def conectarConOdoo():
    server = "localhost"
    port = 8069
    return xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'common'))

def crearNuevaBase(conexion):
    if len(sys.argv) != 2 :
        raise StandardError("Falta el nombre o has pasado algo de mas")
    nombre = sys.argv[1]
    if conexion.db_exist(nombre):
        raise StandardError("Esta base de datos ya existe")
    conexion.create_database('postgres', nombre, True, 'en_GB','admin')

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

def eliminarBase(conexion):
    if len(sys.argv) != 2 :
        raise StandardError("Falta uno nombre o has pasado algo de mas")
    nombre = sys.argv[1]
    if not conexion.db_exist(nombre):
        raise StandardError("La base de datos %s no existe" % (nombre))
    confirmacion = raw_input("Esta seguro de que desea eliminar esta base de datos? S/N \n")
    if confirmacion in ('S'):
        conexion.drop('postgres',nombre)

def obtenerInfoSobreBase(conexion):
    if len(sys.argv) != 2 :
        raise StandardError("Falta uno nombre o has pasado algo de mas")
    nombre = sys.argv[1]
    print(conexion.version())
    print(conexion.about())
    print(conexion.timezone_get(nombre, 'admin', 'admin'))


def listarBases(conexion):
    print 'Listado de bases de datos:'
    l=conexion.list()
    for i in l:
        print i

conn = conectarConOdoo()
obtenerInfoSobreBase(conn)
# crearNuevaBase(conn)
# renombrarBase(conn)
# eliminarBase(conn)

# listarBases(conn)

    # uidUsuario = conexion.authenticate(nombre, 'admin','admin',{})
    # uidUsuario.version()