DELIMITER /
CREATE PROCEDURE sp_insert_time(
	IN varname VARCHAR(15), 
	IN varcode VARCHAR(2))
BEGIN
	INSERT INTO t_type(
		type_name,
		type_code)
	VALUES(
		varname,
		varcode);

END /
DELIMITER ;