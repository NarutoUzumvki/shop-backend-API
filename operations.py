from connection import connection
from utils import *

cursor = connection.cursor()

def add_item(data):
    item_no = generate_item_no()
    deal_no = generate_deal_no()
    data.append(item_no)
    # print(product, price, quantity, item_no)

    add_to_shop_query = """
    insert into shop(`Product`, `Price`, `Quantity`, `Item No`)
    values(%s, %s, %s, %s)
    """
    cursor.execute(add_to_shop_query, data)

    get_qty_query = "select `Quantity` from shop where `Item No` = %s"
    cursor.execute(get_qty_query, item_no)
    qty = cursor.fetchone()

    # if qty:
    #     qty = qty[0]

    add_to_deal_query = """
    insert into dealing_items(`Item No`, `Qty_Added`, `Deal No`)
    values(%s, %s, %s)
    """
    cursor.execute(add_to_deal_query,(item_no, qty[0], deal_no))
    

def get_item_details(item_no):
    retrieve_data_query = """
    select * from shop where `Item No`=%s
    """
    cursor.execute(retrieve_data_query, item_no)
    data = cursor.fetchone()
    if data :
        column_names = [column[0] for column in cursor.description]
        data = dict(zip(column_names, data))
    return data


def update_item(price, quantity, item_no):
    query = """
    update shop set `Price`=%s, `Quantity`=%s where `Item No`=%s
    """
    cursor.execute(query,(price, quantity, item_no)) #####

    get_quantity_query = """
    select `Quantity` from shop where `Item No`=%s
    """
    cursor.execute(get_quantity_query, item_no)

    new_quantity = cursor.fetchone()

    if new_quantity:
        new_quantity = new_quantity[0]
    
    update_deal_query ="""
    update dealing_items set `Qty_Added`=%s where `Item No`=%s
    """
    cursor.execute(update_deal_query, (new_quantity, item_no))


def remove_item(item_no):
    query = """
    delete from shop where `Item No`=%s
    """
    cursor.execute(query, item_no)


def purchase_item(item_no, qty):
    deal_no = generate_deal_no()
    get_quantity_query = """
    select `Quantity` from shop where `Item No`=%s
    """
    cursor.execute(get_quantity_query, item_no)
    previous_quantity = cursor.fetchone()

    new_quantity = previous_quantity[0] - qty

    update_shop_query = """
    update shop set `Quantity`= %s where `Item No`=%s
    """
    cursor.execute(update_shop_query, (new_quantity, item_no))

    data = [item_no, qty]
    data.append(deal_no)
    insert_to_deal_query = """
    insert into dealing_items(`Item No`, `Qty_Purchased`, `Deal No`)
    values(%s, %s, %s)
    """
    cursor.execute(insert_to_deal_query, data)