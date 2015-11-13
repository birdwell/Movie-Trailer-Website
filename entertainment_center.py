import media
import fresh_tomatoes

# Create movies list
movies = []


def add_movie(movie):
    # Add movie to movies list
    movies.append(movie)

# Add movies
add_movie(
    media.Movie(
        'Hitch',
        'https://www.youtube.com/watch?v=dMaq_pfxs-0',
        'http://images.moviepostershop.com/hitch-movie-poster-2005-1020243939.jpg',
        '2005'
    )
)
add_movie(
    media.Movie(
        'IRobot',
        'https://www.youtube.com/watch?v=s0f3JeDVeEo',
        'https://upload.wikimedia.org/wikipedia/en/3/3b/Movie_poster_i_robot.jpg',
        '2004'
    )
)

# Open movies page
fresh_tomatoes.open_movies_page(movies)
