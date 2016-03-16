#!/usr/bin/python
# coding: utf-8
#
import xmlrpclib
import sys
# Datos de conexión (adaptar a cada caso)
#
server = "localhost"
port = 8069
dbname = "bd2"
user_name = "admin"
user_passwd= "postgres"

if len(sys.argv) != 2 :
    raise StandardError("Faltan argumentos o hay de mas")
nombreEmpleado = sys.argv[1]
conn = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'common'))
uid = conn.authenticate(dbname, user_name, user_passwd, {})
object = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'object'))

idContacto = {}
idContacto = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'search_read',
                             [[['name','=',nombreEmpleado]]],{'fields':['name']})
if len(idContacto) != 1 :
    raise Exception("Deberia haber una persona con ese nombre")

print idContacto[0]['id']
sino = raw_input("Esta seguro de que desea borrar a ese contacto? \n")
if sino in ('Si','si','S'):
    object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'unlink', [[idContacto[0]['id']]])
    compania = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'search_read', [[['id','=',idContacto[0]['id']]]])
    print('Partners con el id' + str(idContacto[0]['id']) + ' : ' + str(compania))
