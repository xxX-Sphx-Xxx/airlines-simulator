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
fhubcat="cat_hub.dat"
if os.path.isfile(fhubcat):
	try:
		cnx = mysql.connector.connect(**db_config)
		cursor = cnx.cursor()
		with open(fhubcat,"r") as f:
			for ligne in f.readlines():
				variata = ligne.split(",")[1]
				varhubcategorie = ligne.split(",")[3]
				update_hub_cat="UPDATE t_hub SET hub_categorie_id=%s WHERE hub_iata=%s"
				cursor.executemany(update_hub_cat, (varhubcategorie,variata))
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