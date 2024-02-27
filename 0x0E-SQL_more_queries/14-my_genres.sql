-- script that uses the hbtn_0d_tvshows database
-- lists all genres of the show `Dexter`
-- Result sorted in ascending order by the genre name
SELECT tv_genres.name
FROM tv_genres, tv_shows, tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
AND tv_shows.id = tv_show_genres.show_id
AND tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
