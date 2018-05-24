DELIMITER /
CREATE PROCEDURE sp_select_hub(
	IN var_name VARCHAR(30),
	IN var_rayon INT(5),
	IN var_vitesse INT(3),
	IN var_capacité INT(3),
	IN var_achat INT(9),
	IN var_location INT(9),
	IN var_catid INT(3)
	IN var_type INT(1))
BEGIN
	INSERT INTO t_avion(
		avion_nam,
		avion_rayon,
		avion_vitesse,
		avion_capacité,
		avion_achat,
		avion_location,
		avion_categorie_id,
		avion_type)
	VALUES(
		var_name,
		var_rayon,
		var_vitesse,
		var_capacité,
		var_achat,
		var_location,
		var_catid,
		var_type);
END /
DELIMITER ;