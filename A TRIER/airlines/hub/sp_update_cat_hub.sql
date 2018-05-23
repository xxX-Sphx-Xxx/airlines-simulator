DELIMITER $$
CREATE PROCEDURE sp_update_cat_hub(IN variata INT(2), IN varcat INT(2))
BEGIN
	UPDATE t_hub SET hub_categorie_id = varcat WHERE hub_iata = variata;
END $$
DELIMITER ;