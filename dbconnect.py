#!/usr/bin/python3
#!/usr/bin/env python3

import mysql.connector as mysql

def connectdb() :

	conn = mysql.connect(user='root',password='q',database='attendance',host='localhost')
	conn.cursor()
	sql_lang.execute("show databases;")
	sql_lang.fetchall()
	sql_lang.execute("show tables;")
	conn.commit()

	#check the connection with database
	if conn.is_connected():
		print("Database Connection is established")

	return conn
