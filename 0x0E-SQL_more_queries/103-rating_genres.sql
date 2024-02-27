-- script that lists all genres in the database hbtn_0d_tvshows_rate
-- by their rating
-- Results sorted in descending order by their rating
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS "rating"
FROM tv_genres, tv_show_ratings, tv_shows, tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
AND tv_shows.id = tv_show_genres.show_id
AND tv_shows.id = tv_show_ratings.show_id
AND tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
