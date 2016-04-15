#!/usr/bin/python 
# coding: utf-8 
#
import xmlrpclib

# Datos de conexión (adaptar a cada caso)
#
server = "localhost"
port = 8069
dbname = "bd2"
user_name = "admin"
user_passwd= "postgres"


# Conectamos con el servicio 'common' de Odoo
conn = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'common'))
# Obtenemos identificador (uid) del usuario
uid = conn.authenticate(dbname, user_name, user_passwd, {})
# Conectamos con el servicio 'object' de Odoo
object = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'object'))   

# Buscamos los clientes que son compañías:
customer_ids = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'search', [[['customer', '=' ,True], ['is_company', '=' ,True]]])

# Leemos los nombres de los clientes:
customers = object.execute_kw(dbname, uid, user_passwd,'res.partner', 'read', [customer_ids], {'fields':['name']})

# Y los mostramos:
print "-- Companias --"
for customer in customers:
    print customer['name']

