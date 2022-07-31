from application.dao.model.genre import Genre


class GenreDAO:
    """
    DAO Genre
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_by_id(self, genre_id):
        return self.session.query(Genre).filter(Genre.id == genre_id).one()
