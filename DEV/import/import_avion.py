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

favion="avion.dat"
if os.path.isfile(favion):
	try:
		cnx = mysql.connector.connect(**db_config)
		cursor = cnx.cursor()
		with open(favion,"r") as f:
			for ligne in f.readlines():
				var_name,var_rayon,var_vitesse,var_capacité,var_achat,var_location,var_catid,var_type = ligne.split(",")
				varavion = [var_name,int(var_rayon),int(var_vitesse),int(var_capacité),int(var_achat),int(var_location),int(var_catid),int(var_type)]
				cursor.callproc('sp_insert_avion',varavion)
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
