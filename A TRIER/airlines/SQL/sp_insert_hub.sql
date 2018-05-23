DELIMITER /
CREATE PROCEDURE sp_insert_hub(IN var_hubshortname VARCHAR(100),IN var_hubiata VARCHAR(3), IN var_hublatitude FLOAT(20,18),IN var_hublongitude FLOAT(20,18),IN var_hubpays VARCHAR(100))
BEGIN
	DECLARE var_paysid INT(3);
	SELECT pays_id INTO var_paysid FROM t_pays WHERE pays_name = var_hubpays;
	INSERT INTO t_hub(hub_shortname,hub_iata,hub_latitude,hub_longitude,pays_id)VALUES(var_hubshortname,var_hubiata,var_hublatitude,var_hublongitude,var_paysid);
END /
DELIMITER ;