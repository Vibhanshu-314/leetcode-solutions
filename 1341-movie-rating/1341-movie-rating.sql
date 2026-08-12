SELECT results
FROM (
    SELECT name AS results, 1 AS priority
    FROM Users
    JOIN MovieRating
        ON Users.user_id = MovieRating.user_id
    GROUP BY Users.user_id, Users.name
    ORDER BY COUNT(*) DESC, name
    LIMIT 1
) AS A

UNION ALL

SELECT results
FROM (
    SELECT title AS results, 2 AS priority
    FROM Movies
    JOIN MovieRating
        ON Movies.movie_id = MovieRating.movie_id
    WHERE created_at >= '2020-02-01'
      AND created_at < '2020-03-01'
    GROUP BY Movies.movie_id, Movies.title
    ORDER BY AVG(rating) DESC, title
    LIMIT 1
) AS B;