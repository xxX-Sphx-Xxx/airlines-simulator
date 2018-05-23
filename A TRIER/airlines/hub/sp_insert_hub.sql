DELIMITER $$
CREATE PROCEDURE sp_insert_hub(IN varshortname VARCHAR(50), IN varlongname VARCHAR(100), IN variata VARCHAR(3), IN varlatiutude INTEGER(20), IN varlongitude INTEGER(20))
BEGIN
CALL sp_select_pays_id(@@a);
SELECT @a INTO p_id FROM dual;
INSERT INTO t_hub(hub_shortname,hub_longname,hub_iata,hub_latitude,hub_longitude,hub_pays_id,hub_categorie_id ) VALUES(varshortname, varlongname, variata, varlatiutude, varlongitude, p_id,1);
END $$
DELIMITER ;

