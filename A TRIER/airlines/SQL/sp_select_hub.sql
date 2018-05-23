DELIMITER $$

CREATE PROCEDURE 'sp_select_hub'

1 - SELECT h.shortname, h.iata,p.name,c.catlibelle FROM hub + pays 
WHERE iata = variata, 