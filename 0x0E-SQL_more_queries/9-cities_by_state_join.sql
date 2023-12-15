-- A script that uses a join method
SELECT `cities`.`id`, `cities`.`name`,`states`.`order_id` FROM `cities` INNER JOIN `states` ON `cities`.`state_id`= `state`.`id` ORDER BY `cities`.`id`