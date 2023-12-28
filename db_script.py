from connection import connection

cursor = connection .cursor()

create_shop_query = """
create table `shop`(
    `Item No` varchar(8) NOT NULL PRIMARY KEY,
    `Product` varchar(35) NOT NULL ,
    `Price` int NOT NULL,
    `Quantity` int NOT NULL
)
"""

# cursor.execute(create_shop_query)

insert_to_shop_query = """
insert into shop (`Item No`, `Product`, `Price`, `Quantity`)
values("ad47frg6", "Cream", 50, 20)
"""
# cursor.execute(insert_to_shop_query)


create_dealing_items_query = """
create table `dealing_items`(
    `Deal No` varchar(6) NOT NULL PRIMARY KEY,
    `Item No` varchar(8) NOT NULL,
    `Qty_Added` int DEFAULT NULL,
    `Qty_Purchased` int DEFAULT NULL, 
    `Time` DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`Item No`) REFERENCES shop(`Item No`)
)
"""

# cursor.execute(create_dealing_items_query)

