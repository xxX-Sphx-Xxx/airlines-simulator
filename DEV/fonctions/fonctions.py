#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


#Fonctions de conversion
def deg2rad(degree):
  """Convertir des degrés en radian"""
	return (degree * pi)/180
def heure2deci(heure,minute):
  """Converti des heures,minutes en décimal"""
  return heure + ( minute / 60 )
def deci2heure(deci):
  """Converti des décimales en heure minute"""
  heure = trunc(deci)
  minutes = (deci - trunc(deci)) * 60

#Fonction calcul physique
def hub_distance(latitude1, longitude1, latitude2, longitude2):
  """ Fonction qui calcul la distance entre deux aéroports en utilisant la latidue et la longitude et un rayon de 6378 Km """
  rayon = 6378
  distance = acos(sin(deg2rad(latitude1))*(sin(deg2rad(latitude2)))+cos(deg2rad(latitude1))*cos(deg2rad(latitude2))*cos(deg2rad(longitude1) - deg2rad(longitude2))) * rayon
  return distance
def tj(distance, vitesse):
  """Fonction qui calcul le temps de trajet d'un avion"""
  temps_deci = distance / vitesse
  temps_heure = trunc(temps_deci)
  temps_minutes = (temps_deci - trunc(temps_deci)) * 60
  aff_heure(temps_heure,trunc(temps_minutes))

#Fonction d'affichage
def aff_heure(heure,minute):
  """Affiche l'heure dans un format heure:minute"""
  return print("{}:{}".format(heure,minute))

#Fonction de recherche
