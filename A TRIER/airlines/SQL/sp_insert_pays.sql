DELIMITER /
CREATE PROCEDURE sp_insert_pays(IN var_name VARCHAR(50), IN var_code INT(3))
BEGIN
	INSERT INTO t_pays(pays_name,pays_code) VALUES(var_name,var_code);
END /
DELIMITER ;