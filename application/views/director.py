from flask_restx import Resource, Namespace

from application.dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        """
        Получение списка всех режиссёров
        """
        return director_schema.dump(director_service.get_all()), 200


@director_ns.route('/<int:director_id>/')
class DirectorView(Resource):
    def get(self, director_id: int):
        """
        Получение режиссера по его id
        """
        return director_schema.dump([director_service.get_by_id(director_id)]), 200
