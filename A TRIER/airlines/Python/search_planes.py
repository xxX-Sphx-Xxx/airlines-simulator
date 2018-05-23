#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mysql.connector
from mysql.connector import errorcode
from function import hub_distance

Formulaire :
Hub de départ (varhubdepart) :
Hub de destination (varhubdestination) :
Nombre de passager eco (p_eco):
Nombre de passager business (p_business) :
Nombre de passager first (p_first) :

1 - calculer distance
2 - Calculer total PAX (varpax)
3 - Selectionner les avions par distance et total pax

1 -
	try:
		cnx = mysql.connector.connect(**db_config)
		cursor = cnx.cursor()
		cursor.callproc('sp_select_HubByCoord',varhubdepart,varhubdestination,latitude_depart,longitude_depart,latitude_destination,longitude_destination)
		#rows = cursor.fetchall()
		vardistance = hub_distance(latitude_depart,longitude_depart,latitude_destination,longitude_destination)
		#for latitude_depart,longitude_depart,latitude_destination,longitude_destination in rows:
		#	hub_distance(latitude_depart,longitude_depart,latitude_destination,longitude_destination)
2 -
		varpax = p_eco + p_business + p_first
3 -
		cursor.callproc('sp_select_AvionByRayonAndCapacite',vardistance,varpax)
		resultats = cursor.fetchall
		for avion_name, avion_rayon, avion_capacité in resultats:
			print("Nom :{}\tRayon d\'action :{}\tCapacité :{}")
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


#mysql_cursor.execute( "call get_lastpoll();" )
#results=mysql_cursor.fetchone()
#print results[0]
