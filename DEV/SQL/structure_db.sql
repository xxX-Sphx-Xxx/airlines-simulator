#!/usr/bin/env python
# -*- coding: utf-8 -*-

CREATE DATABASE airlines_db CHARACTER SET utf8;
CREATE user Air_UserADM;
GRANT all ON airlines_db.* TO 'Air_UserADM'@'localhost' IDENTIFIED BY '819bbe731f328d9b15873627e7b5c5dd';
USE airlines_db;
CREATE TABLE IF NOT EXISTS t_pays (
	pays_id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY (pays_id) ,
	pays_name VARCHAR (50) NULL DEFAULT NULL ,
	pays_code VARCHAR(2) NULL DEFAULT NULL ,
	FULLTEXT ind_pays_name (pays_name),
	FULLTEXT ind_payx_name(pays_code)) ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS t_categorie (
	categorie_id INT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY (categorie_id) ,
	categorie_numero INT(2) NULL DEFAULT NULL ,
	categorie_libelle VARCHAR(10) NULL DEFAULT NULL ,
	INDEX ind_categorie_numero (categorie_numero)) ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS t_time (
	time_id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY (time_id) ,
	time_heure INT(2) NULL DEFAULT NULL ,
	time_minute INT(2) NULL DEFAULT NULL ,
	time_decimal DECIMAL(4,2)
	INDEX ind_time_decimal (time_decimal) ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS t_hub (
	hub_id INT(3) AUTO_INCREMENT PRIMARY KEY(hub_id) ,
	hub_shortname VARCHAR(50) NULL DEFAULT NULL ,
	hub_longname VARCHAR(50) NULL DEFAULT NULL ,
	hub_iata VARCHAR(3) NULL DEFAULT NULL ,
	hub_latitude DECIMAL(20,17) NULL DEFAULT NULL ,
	hub_longitude DECIMAL(20,17) NULL DEFAULT NULL ,
	hub_pays_id INT(3) NULL DEFAULT NULL ,
	hub_categorie_id INT(3) NULL DEFAULT NULL ,
	CONSTRAINT fk_hub_pays FOREIGN Key (hub_pays_id) REFERENCES t_pays(pays_id)  ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT fk_hub_categorie FOREIGN KEY (hub_categorie_id) REFERENCES t_categorie(categorie_id) ON DELETE SET NULL ON UPDATE CASCADE
	) ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS t_type (
	type_id INT(1) AUTO_INCREMENT PRIMARY KEY(type_id),
	type_name VARCHAR(15) NULL DEFAULT NULL,
	type_code VARCHAR(2) NULL DEFAULT NULL,
	FULLTEXT ind_type_name (type_name),
	FULLTEXT ind_type_code (type_code)
	) ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS t_avion (
	avion_id INT(3) AUTO_INCREMENT PRIMARY KEY(avion_id) ,
	avion_name VARCHAR(30) NULL DEFAULT NULL ,
	avion_rayon INT(5) NULL DEFAULT NULL ,
	avion_vitesse INT(3) NULL DEFAULT NULL ,
	avion_capacité INT(3) NULL DEFAULT NULL ,
	avion_achat INT(9) NULL DEFAULT NULL ,
	avion_location INT(9) NULL DEFAULT NULL ,
	avion_categorie_id INT(3) NULL DEFAULT NULL ,
	avion_type_id INT(1) NULL DEFAULT NULL,
	CONSTRAINT fk_avion_categorie_id FOREIGN KEY(avion_categorie_id) REFERENCES t_categorie(categorie_id) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT fk_avion_type_id FOREIGN KEY(avion_type_id) REFERENCES t_type(type_id) ON DELETE SET NULL ON UPDATE CASCADE
	) ENGINE = InnoDB;
