import os
import mysql.connector
from mysql.connector import errorcode

db_config = {
	'user':'Air_UserADM',
	'password':'819bbe731f328d9b15873627e7b5c5dd',
	'host':'localhost',
	'database':'Airlines_db'}
fhub="hub.dat"
if os.path.isfile(fhub):
	try:
		cnx = mysql.connector.connect(**db_config)
		cursor = cnx.cursor()
		with open(fhub,"r") as f:
			for ligne in f.readlines():
				varhubshortNAME = ligne.split(",")[1]
				varpays = ligne.split(",")[3]
				varhubiata = ligne.split(",")[4]
				varhublatitude = ligne.split(",")[6]
				varhublongitude = ligne.split(",")[7]
				varhubcategorie = ""
				varhublongNAME = varhubiata + " , " + varhubshortNAME + varhubcategorie
				varhub = [varhubshortNAME, varhublongNAME, varhubiata, varhublatitude, varhublongitude]
				cursor.callproc('sp_select_pays_id',varpays)
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

# db_config = {
# 	'user':'Air_UserADM',
# 	'password':'819bbe731f328d9b15873627e7b5c5dd',
# 	'host':'localhost',
# 	'database':'Airlines_db'}
# cnx = mysql.connector.connect(**db_config)
# cursor = cnx.cursor()
# varhub = ["Charles de Gaulle", "CDG , Charles de Gaulle", "CDG", "49.0127983093", "2.54999995232", 426, 1]
# cursor.callproc('sp_insert_hub',varhub)
# cnx.commit()
# cursor.close()
# cnx.close()