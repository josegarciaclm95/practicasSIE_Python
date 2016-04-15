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

conn = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'common'))
uid = conn.authenticate(dbname, user_name, user_passwd, {})
object = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'object'))

idContacto = {}
idContacto = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'search_read',
                             [[['name','=','Agrolait']]],{'fields':['child_ids']})
print idContacto

childs_id = idContacto[0]['child_ids']
for id in childs_id:
    datosContacto = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'search_read',
                             [[['id','=',id]]],{'fields':['name','type','email','city']})
    nombre = datosContacto[0]['name']
    tipo = datosContacto[0]['type']
    email = datosContacto[0]['email']
    ciudad = datosContacto[0]['city']
    print("Nombre: "+ nombre + "\t Tipo: " + tipo + "\t Correo electronico: " + email + "\t Ciudad: "+ ciudad)