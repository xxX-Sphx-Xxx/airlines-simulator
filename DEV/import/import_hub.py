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

fhub="hub_test.dat"
if os.path.isfile(fhub):
	try:
		cnx = mysql.connector.connect(**db_config)
		cursor = cnx.cursor()
		with open(fhub,"r",encoding="utf8") as f:
			for ligne in f.readlines():
				var_hubshortname = ligne.split(",")[0]
				var_hubpays = ligne.split(",")[2]
				var_hubiata = ligne.split(",")[3].strip()
				if var_hubiata == "":
					var_hubiata = "ZZZ"
				var_hublatitude = ligne.split(",")[5]
				var_hublongitude = ligne.split(",")[6]
				varhub = [var_hubshortname,var_hubiata,var_hublatitude,var_hublongitude,var_hubpays]
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