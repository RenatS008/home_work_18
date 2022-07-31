from application.dao.genre_dao import GenreDAO
from application.dao.model.genre import Genre


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_by_id(self, genre_id):
        return self.genre_dao.get_by_id(genre_id)

    def get_all(self) -> list[Genre]:
        return self.genre_dao.get_all()
