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

def import_hub(file):
	db_config = {
	'user'='Air_UserADM',
	'password'='819bbe731f328d9b15873627e7b5c5dd',
	'host'='localhost',
	'database'='Airlines_db'}
	if file_existe(file):
		ofile = open(file,"r")
		ligne = ofile.readline()
		varhubshortNAME = ligne.split(",")[1]
		varhubcategorie = ""
		varpays = ""
		varhubiata = ligne.split(",")[4]
		varhublatitude = ligne.split(",")[6]
		varhublongitude = ligne.split(",")[7]
		varhublongNAME = varhubiata + " , " + varhubshortNAME + varhubcategorie
		varhub = {
		'shortName':varhubshortNAME,
		'longNAME':varhublongNAME,
		'paysid':varpays,
		'catid':varhubcategorie,
		'iata':varhubiata,
		'latitude':varhublatitude,
		'longitude':varhublongitude
		}
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
		cursor.execute("INSERT INTO hub(shortNAME,longNAME,paysid,catid,iata,latitude,longitude) VALUES(?,?,?,?,?,?)",varhub)
		cnx.comit
		cursor.execute ("SELECT * FROM hub")
		rows = cursor.fetchall()
		for row in rows:
			print row
		cursor.close()
		cnx.close()
	else:
		print("Le fichier n'existe pas")
