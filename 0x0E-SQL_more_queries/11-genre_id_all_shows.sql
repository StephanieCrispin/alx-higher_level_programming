-- Lists all shows in hbtn_02_shows database
-- Returns null if a show has not yet been assigned a genre
SELECT s.`title`, g.`genre_id`
 FROM `tv_shows` AS s
    LEFT JOIN `tv_show_genres` AS g
    ON s.`id`=g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
