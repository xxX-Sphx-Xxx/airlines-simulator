DELIMITER $$

CREATE PROCEDURE sp_select_pays_id(IN varpays VARCHAR(50), OUT varpaysid INT(3))
BEGIN
SELECT pays_id INTO varpaysid FROM t_pays WHERE pays_name = varpays;
END $$
DELIMITER ;
