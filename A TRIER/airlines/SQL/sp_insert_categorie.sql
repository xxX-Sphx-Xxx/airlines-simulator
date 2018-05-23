DELIMITER /
CREATE PROCEDURE sp_insert_categorie(IN var_catnum INT(2), IN var_catlib VARCHAR(10))
BEGIN
	INSERT INTO t_categorie(categorie_numero,categorie_libelle) VALUES(var_catnum,var_catid);
END /
DELIMITER ;