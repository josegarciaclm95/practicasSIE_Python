#!/usr/bin/python 
# coding: utf-8 
#
# listar DBs

import xmlrpclib


# Datos de conexión
#
server = "localhost"
port = 8069


conn = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'db'))
print 'Listado de bases de datos:'
l=conn.list()
for i in l:
    print i









