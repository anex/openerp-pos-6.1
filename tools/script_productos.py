import xmlrpclib
import base64
import Image

dbname = "PDVAL"
username = "admin"
pwd = "123321..."

sock_common = xmlrpclib.ServerProxy ('http://192.168.113.184:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)

sock = xmlrpclib.ServerProxy('http://192.168.113.184:8069/xmlrpc/object')

entrada = open("PDVAL1.csv")

for each in entrada.readlines()[1:]:
    try:

        vals = each.split(",")
        default_code = vals[0]
        ean13 = vals[1]
        name_template = vals[2]
        print name_template
        list_price = vals[4][:-1]
        f = open("fotos_pdval1/"+str(ean13)+".jpg")
        product_image = base64.b64encode(f.read())
        f1 = Image.open("fotos_pdval1/"+str(ean13)+".jpg")
        f1.thumbnail((100,100))
        f1.save("fotos_pdval1/"+str(ean13)+"_small.jpg")
        f2 = open("fotos_pdval1/"+str(ean13)+"_small.jpg")
        product_image_small = base64.b64encode(f2.read())

        data = {
                 'ean13':ean13,
                 'list_price':list_price,
                 'default_code':default_code,
                 'code':default_code,
                 'name_template':name_template,
                 'name':name_template,
                 'product_image':product_image,
                 'product_image_small':product_image_small,
                 'warranty': 0.0,
                 'supply_method': 'buy',
                 'uos_id': False,
                 'weight': 0.0,
                 'color': 0,
                 'incoming_qty': 0.0,
                 'cost_method': 'standard',
                 'active': True,
                 'price_extra': 0.0,
                 'mes_type': 'fixed',
                 'description_purchase': False,
                 'property_account_income': False,
                 'expense_pdt': False,
                 'variants': False,
                 'uos_coeff': 1.0,
                 'type': 'product',
                 'sale_ok': True,
                 'purchase_ok': True,
                 'product_manager': False,
                 'track_outgoing': False,
                 'produce_delay': 1.0,
                 'state': False,
                 'loc_rack': False,
                 'income_pdt': False,
                 'price_margin': 1.0,
                 'property_stock_account_input': False,
                 'loc_case': False,
                 'description': False,
                 'track_incoming': False,
                 'volume': 0.0,
                 'outgoing_qty': 0.0,
                 'loc_row': False,
                 'seller_info_id': False,
                 'procure_method': 'make_to_stock',
                 'seller_qty': 0.0,
                 'valuation': 'manual_periodic',
                 'seller_delay': 1,
                 'weight_net': 0.0,
                 'seller_id': False,
                 'sale_delay': 7.0,
                 'description_sale': False,
                 'property_account_expense': False,
                 'track_production': False,
                 'price': 0.0,
                 'property_stock_account_output': False,
                 'rental': False
                }

        product_id = sock.execute(dbname, uid, pwd, 'product.product', 'create', data)
    except IOError:
        print "Hubo problema con ",ean13 

