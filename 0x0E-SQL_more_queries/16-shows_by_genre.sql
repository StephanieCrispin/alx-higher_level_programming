-- Lists all shows in hbtn_02_shows database
-- Returns null if a show has not yet been assigned a genre
SELECT s.`title`,w.`name`
 FROM `tv_shows` AS s
    LEFT JOIN `tv_show_genres` AS g
    ON s.`id` = g.`show_id`

    LEFT JOIN `tv_genres` AS w
    ON g.`genre_id`=w.`id`
ORDER BY s.`title`, w.`name`;
