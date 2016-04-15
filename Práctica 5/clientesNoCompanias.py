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


conn = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'common'))
uid = conn.authenticate(dbname, user_name, user_passwd, {})
object = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'object'))

customer_notCompanies = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'search', [[['customer', '=' ,True],
                                                                                               ['is_company', '=' ,False]]])

# Leemos los nombres de los clientes:
customers = object.execute_kw(dbname, uid, user_passwd,'res.partner', 'read', [customer_notCompanies], {'fields':['name','email']})

# Y los mostramos:
print "----- Clientes que no son companias -----"
for customer in customers:
    print customer['name'],'\t -> \t', customer['email']

