from flask_restx import Resource, Namespace

from application.dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        """
        Получение списка всех жанров
        """
        return genre_schema.dump(genre_service.get_all()), 200


@genre_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    def get(self, genre_id: int):
        """
        Получение жанра по его id
        """
        return genre_schema.dump([(genre_service.get_by_id(genre_id))]), 200
