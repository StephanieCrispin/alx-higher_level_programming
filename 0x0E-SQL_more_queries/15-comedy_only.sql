-- Lists all tv titles under comedy genre
SELECT t.`title`
    FROM `tv_shows` AS t
    INNER JOIN `tv_shows_genres` AS s
    ON t.`id` = s.`show_id`

    INNER JOIN `tv_genres` as g
    ON g.`id` = s.`genre_id`
    WHERE g.`name` = 'Comedy'
ORDER BY t.`title`;
