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
nombreEmpresa = sys.argv[1]
conn = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'common'))
uid = conn.authenticate(dbname, user_name, user_passwd, {})
object = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'object'))

compania = {}
compania = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'search_read',
                             [[['is_company', '=' ,True],['name','=',nombreEmpresa]]],{'fields':['name']})
if len(compania) != 0 :
    raise Exception("Ya existe una empresa con ese nombre")
idCompania = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'create', [{'name': nombreEmpresa,'is_company':True}])
print 'El id de la nueva compania es {0}'.format(idCompania)

nombreContacto = raw_input("Introduzca nombre \n")
calleContacto = raw_input("Introduzca calle \n")
ciudadContacto = raw_input("Introduzca ciudad \n")
telefonoContacto = raw_input("Introduzca telefono \n")
faxContacto = raw_input("Introduzca fax \n")
emailContacto = raw_input("Introduzca email \n")
idContacto = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'create', [{'name': nombreContacto,
                                                                                    'street':calleContacto,
                                                                                    'email':emailContacto,
                                                                                    'fax':faxContacto,
                                                                                    'phone':telefonoContacto,
                                                                                    'parent_id':idCompania,
                                                                                    'city':ciudadContacto,
                                                                                    'type':'contact'
                                                                                     }])
print('El id del contacto es {0}'.format(idContacto))
compania = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'search_read', [[['is_company', '=' ,True],['id','=',idCompania]]],{'fields':['child_ids']})
print('Los ids de los contactos de la empresa son \n',compania)