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

def import_categorie():
	db_config = {
	'user'='Air_UserADM',
	'password'='819bbe731f328d9b15873627e7b5c5dd',
	'host'='localhost',
	'database'='Airlines_db'}
	varcategorie = {
	1:"Cat. 1)",
	2:"Cat. 2)",
	3:"Cat. 3)",
	4:"Cat. 4)",
	5:"Cat. 5)",
	6:"Cat. 6)",
	7:"Cat. 7)",
	8:"Cat. 8)",
	9:"Cat. 9)",
	10:"Cat. 10)"
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
	cursor.execute("INSERT INTO categorie(catnumero,catlibelle) VALUES(?,?)",varcategorie)
	cat_no = cursor.lastrowid
	cnx.comit
	for (catnumero, catlibelle) in cursor:
		print(" Numéro Catégorie: {}\tLibellé: {}".format(catnumero, catlibelle)
	cursor.close()
	cnx.close()


def import_hub(file):
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
		cursor.execute()
	else:
		print("Le fichier n'existe pas")	



hub :

hubshortNAME = ligne.split(",")[1]
hubcategorie = "(Cat. 10)"
hubiata = ligne.split(",")[4]
hublatitude = ligne.split(",")[6]
hublongitude = ligne.split(",")[7]
hublongNAME = hubiata + " , " + hubshortNAME + hubcategorie

print("{} \t{} \t{} \t{} \t{} \t{}".format(hubshortNAME,hubcategorie,hublongNAME,hubiata,hublatitude,hublongitude))