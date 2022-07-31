from application.dao.director_dao import DirectorDAO
from application.dao.genre_dao import GenreDAO
from application.dao.movie_dao import MovieDAO
from application.service.director import DirectorService
from application.service import GenreService
from application.service import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao=movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao=genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao=director_dao)
