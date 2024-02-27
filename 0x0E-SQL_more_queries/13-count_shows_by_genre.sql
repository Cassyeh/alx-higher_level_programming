-- script that lists all genres from hbtn_0d_tvshows
-- displays the number of shows linked to each genre
-- Doesn't display a genre that doesn’t have any shows linked
-- Result sorted in descending order by the number of shows linked
SELECT tv_genres.name AS 'genre',
COUNT(tv_show_genres.genre_id) AS "number_of_shows"
FROM tv_genres, tv_shows, tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
AND tv_shows.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
