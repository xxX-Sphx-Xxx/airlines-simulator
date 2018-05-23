DELIMITER $$
CREATE PROCEDURE sp_insert_hub(IN varheure INT(2), IN varminute INT(2), IN vardecimal INT(20))
BEGIN
	INSERT INTO t_time(heure,minute,h_m_decimal) VALUES(varheure, varminute, vardecimal)

END $$
DELIMITER ;

