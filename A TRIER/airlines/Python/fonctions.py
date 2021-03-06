#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


def deg2rad(degree):
	return (degree * pi)/180

def hub_distance(latitude1, longitude1, latitude2, longitude2):
	""" Fonction qui calcul la distance entre deux aéroports en utilisant la latidue et la longitude et un rayon de 6378 Km """
	rayon = 6378
	distance = acos(sin(deg2rad(latitude1))*(sin(deg2rad(latitude2)))+cos(deg2rad(latitude1))*cos(deg2rad(latitude2))*cos(deg2rad(longitude1) - deg2rad(longitude2))) * rayon
	return distance

def aff_heure(heure,minute):
  return print("{}:{}".format(heure,minute))
  
def tj(distance, vitesse):
  temps_deci = distance / vitesse
  temps_heure = trunc(temps_deci)
  temps_minutes = (temps_deci - trunc(temps_deci)) * 60
  aff_heure(temps_heure,trunc(temps_minutes))

def heure2deci(heure,minute):
  return heure + ( minute / 60 )

def deci2heure(deci):
  heure = trunc(deci)
  minutes = (deci - trunc(deci)) * 60