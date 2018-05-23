#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mysql.connector
from mysql.connector import errorcode

db_config = {
	'user':'Air_UserADM',
	'password':'819bbe731f328d9b15873627e7b5c5dd',
	'host':'localhost',
	'database':'Airlines_db'}

ftime="time.dat"
if os.path.isfile(ftime):
	try:
		cnx = mysql.connector.connect(**db_config)
		cursor = cnx.cursor()
		with open(ftime,"r") as f:
			for ligne in f.readlines():
				varheure = ligne.split(",")[0]
				varminute = ligne.split(",")[1]
				
				cursor.callproc('sp_insert_hub',varhub)
		cnx.commit()
		cursor.close()
		cnx.close()
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something's wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		cnx.close()