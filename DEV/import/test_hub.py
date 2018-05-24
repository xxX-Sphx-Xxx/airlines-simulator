#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
fhub="hub_test.dat"
if os.path.isfile(fhub):
	with open(fhub,"r",encoding="utf8") as f:
		for ligne in f:
			var_hubshortname = ligne.split(",")[0]
			var_hubpays = ligne.split(",")[2]
			var_hubiata = ligne.split(",")[3].strip()
			if var_hubiata == "":
				var_hubiata = "ZZZ"
			var_hublatitude = ligne.split(",")[5]
			var_hublongitude = ligne.split(",")[6]
			varhub = [var_hubshortname,var_hubpays,var_hubiata,var_hublatitude,var_hublongitude]
			print("{}\t{}\t{}\t{}\t{}".format(var_hubshortname,var_hubpays,var_hubiata,var_hublatitude,len(var_hublongitude))
else:
	print("Not a file")