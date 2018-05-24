DELIMITER $$
CREATE PROCEDURE sp_insert_time(IN varheure INT(2), IN varminute INT(2), IN vardecimal DECIMAL(4,2))
BEGIN
	INSERT INTO t_time(time_heure,time_minute,time_decimal) VALUES(varheure, varminute, vardecimal);

END $$
DELIMITER ;