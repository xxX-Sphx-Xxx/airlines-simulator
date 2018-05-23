#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mysql.connector
from mysql.connector import errorcode

def file_existe(file):
	try:
		ofile = open(file,"r")
		ofile.close()
		return 1
	except:
		return 0

def import_pays(file):
	db_config = {
	'user'='Air_UserADM',
	'password'='819bbe731f328d9b15873627e7b5c5dd',
	'host'='localhost',
	'database'='Airlines_db'}
	if file_existe(file):
		ofile = open(file,"r")
		ligne = ofile.readline()
		varname=ligne.split(",")[0]
		varcode=ligne.split(",")[1]
		varpays = {varname : varcode}
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
		cursor.execute("INSERT INTO pays(name,code) VALUES(?,?)",varpays)
		pays_no = cursor.lastrowid
		cnx.comit
		for (name, code) in cursor:
			print(" Pays: {}\tCode: {}".format(name, code)
		cursor.close()
		cnx.close()
	else:
		print("Le fichier n'existe pas")