DELIMITER /
CREATE PROCEDURE sp_insert_time(
	IN variata VARCHAR(3), 
	IN varcat INT(3))
BEGIN
	UPDATE t_hub SET hub_categorie_id = varcat WHERE hub_iata = variata;
END /
DELIMITER ;