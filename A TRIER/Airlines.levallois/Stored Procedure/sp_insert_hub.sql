DELIMITER $$
CREATE PROCEDURE sp_insert_hub(IN varshortname VARCHAR(50), IN varlongname VARCHAR(100), IN variata VARCHAR(3), IN varlatiutude INTEGER(20), IN varlongitude INTEGER(20), IN varpays VARCHAR(50))
{
	DECLARE p_id INT;
	SELECT t_pays.pays_id INTO p_id FROM t_pays WHERE t_pays.pays_name = varpays
}
BEGIN
	INSERT INTO t_hub(hub_shortname,hub_longname,hub_iata,hub_latitude,hub_longitude,hub_pays_id,hub_categorie_id ) VALUES(varshortname, varlongname, variata, varlatiutude, varlongitude, p_id)

END$$

DELIMITER;
