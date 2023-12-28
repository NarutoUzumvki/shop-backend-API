import pymysql

db_config = {
    "user":"root",
    "host":"localhost",
    "password":"SQLP@ssw0rd",
    "database":"shop_data",
    "autocommit":"true"
}

connection = pymysql.connect(**db_config)
