DELIMITER $$

CREATE PROCEDURE sp_select_HubByCoord(IN varhubdepartid INT(3), IN varhubdestinationid INT(3), OUT latitude_depart DECIMAL(20,17), 
	OUT longitude_depart DECIMAL(20,17), OUT latitude_destination DECIMAL(20,17), OUT longitude_destination DECIMAL(20,17))
BEGIN
	SELECT hub_latitude, hub_longitude INTO latitude_depart, longitude_depart
	FROM t_hub
	WHERE hub_id IN (varhubdepartid)
	SELECT hub_latitude,hub_longitude INTO latitude_destination, longitude_destination
	FROM t_hub
	WHERE hub_id IN (varhubdestinationid)
END $$
DELIMITER ;