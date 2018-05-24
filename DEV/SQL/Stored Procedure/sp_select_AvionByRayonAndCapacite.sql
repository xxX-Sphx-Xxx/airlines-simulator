DELIMITER $$

CREATE PROCEDURE sp_select_AvionByRayonAndCapacite(IN vardistance INT(5), IN varcapacite INT(3))
BEGIN
	SELECT avion_id, avion_name, avion_rayon, avion_capacité
	FROM t_avion
	WHERE avion_rayon <= vardistance AND avion_capacite <= varcapacite;
END $$
DELIMITER ;