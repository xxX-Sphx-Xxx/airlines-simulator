#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode

db_config = {
	'user'='Air_UserADM',
	'password'='819bbe731f328d9b15873627e7b5c5dd',
	'host'='localhost',
	'database'='Airlines_db'}
var_categorie = {
	1:"(Cat. 1)",
	2:"(Cat. 2)",
	3:"(Cat. 3)",
	4:"(Cat. 4)",
	5:"(Cat. 5)",
	6:"(Cat. 6)",
	7:"(Cat. 7)",
	8:"(Cat. 8)",
	9:"(Cat. 9)",
	10:"(Cat. 10)"}
try:
	cnx = mysql.connector.connect(**db_config)
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something's wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
else:
	cnx.close()
cursor = cnx.cursor()
cursor.execute("INSERT INTO categorie(catnumero,catlibelle) VALUES(?,?)",var_categorie)
cat_no = cursor.lastrowid
cnx.comit
for (catnumero, catlibelle) in cursor:
	print(" Numéro Catégorie: {}\tLibellé: {}".format(catnumero, catlibelle)
cursor.close()
cnx.close()