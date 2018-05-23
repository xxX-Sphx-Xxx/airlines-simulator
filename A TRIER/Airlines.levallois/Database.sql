#!/usr/bin/env python
# -*- coding: utf-8 -*-

CREATE DATABASE airlines_db;
CREATE user Air_UserADM;
GRANT all ON airlines_db.* TO 'Air_UserADM'@'localhost' IDENTIFIED BY '819bbe731f328d9b15873627e7b5c5dd';

USE airlines_db

CREATE TABLE t_pays ( 
	pays_id INT(3) NOT NULL AUTO_INCREMENT ,
	pays_name VARCHAR(50) NULL DEFAULT NULL ,
	pays_code INT(3) NULL DEFAULT NULL ,
	PRIMARY KEY (pays_id)) ENGINE = InnoDB;
CREATE TABLE t_categorie (
	categorie_id INT(2) NOT NULL AUTO_INCREMENT ,
	categorie_numero INT(2) NULL DEFAULT NULL ,
	categorie_libelle VARCHAR(10) NULL DEFAULT NULL,
	PRIMARY KEY (categorie_id)) ENGINE = InnoDB;
CREATE TABLE t_time (
	time_id INT(2) NOT NULL AUTO_INCREMENT ,
	time_heure INT(2) NULL DEFAULT NULL ,
	time_minute INT(2) NULL DEFAULT NULL ,
	time_decimal FLOAT(4,2) NULL DEFAULT NULL ,
	PRIMARY KEY (time_id)) ENGINE = InnoDB;

CREATE TABLE t_hub (
	hub_id INT(3) NOT NULL AUTO_INCREMENT ,
	hub_shortname VARCHAR(50) NULL DEFAULT NULL , 
	hub_longname VARCHAR(100) NULL DEFAULT NULL ,
	hub_iata VARCHAR(3) NULL DEFAULT NULL ,
	hub_latitude FLOAT(20,18) NULL DEFAULT NULL ,
	hub_longitude FLOAT(20,18) NULL DEFAULT NULL ,
	pays_id INT(3) NOT NULL ,
	categorie_id INT(3) NOT NULL,
	PRIMARY KEY (hub_id) ,
	FOREIGN KEY (pays_id) REFERENCES t_pays(pays_id) ,
	FOREIGN KEY (categorie_id) REFERENCES t_categorie(categorie_id)) ENGINE = InnoDB;

CREATE TABLE t_avion (
	avion_id INT(3) NOT NULL AUTO_INCREMENT ,
	avion_name VARCHAR(30) NULL DEFAULT NULL ,
	avion_rayon VARCHAR(5) NULL DEFAULT NULL , 
	avion_vitesse INT(3) NULL DEFAULT NULL ,
	avion_capacité INT(3) NULL DEFAULT NULL ,
	avion_achat INT(9) NULL DEFAULT NULL ,
	avion_location INT(9) NULL DEFAULT NULL ,
	categorie_id INT(3) NOT NULL ,
	PRIMARY KEY (avion_id),
	FOREIGN KEY (categorie_id) REFERENCES t_categorie(categorie_id)) ENGINE = InnoDB;