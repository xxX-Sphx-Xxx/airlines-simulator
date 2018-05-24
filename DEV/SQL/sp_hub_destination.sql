DELIMITER /
CREATE PROCEDURE sp_rechercher_destination(hub_depart_id INT, hub_categorie_min INT, hub_categorie_max INT, 
	avion_id INT, heure_min_id INT, heure_max_id INT)
BEGIN
	DECLARE v_vit_avion INT;
	DECLARE v_hub_depart_id INT;
	DECLARE v_hub_depart_latitude INT;
	DECLARE v_hub_depart_longitude INT;
	DECLARE v_hub_pays VARCHAR;

	SELECT vitesse INTO v_vit_avion FROM t_avions where avion_id = avion_id;
	SELECT hub_id INTO v_hub_depart_id FROM t_hub where hub_id = hub_depart_id;
	SELECT hub_latitude, hub_longitude, INTO v_hub_depart_latitude, v_hub_depart_longitude from t_hub WHERE hub_id = v_hub_depart_id;
	SELECT t_pays.p_name INTO v_hub_pays FROM t_pays LEFT JOIN t_hub ON t_hub.pays_id = t_pays.pays_id;


END /