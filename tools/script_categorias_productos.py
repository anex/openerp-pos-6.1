import xmlrpclib
import base64
import Image

dbname = "PDVAL"
username = "admin"
pwd = "123321..."

sock_common = xmlrpclib.ServerProxy ('http://192.168.113.184:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)

sock = xmlrpclib.ServerProxy('http://192.168.113.184:8069/xmlrpc/object')

args = [] #query clause
ids = sock.execute(dbname, uid, pwd, 'product.product', 'search', args)

values = {'pos_categ_id': 2}

result = sock.execute(dbname, uid, pwd, 'product.product', 'write', ids, values)





