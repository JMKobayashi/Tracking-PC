from odmantic import Model
from track.infrastructure.repositories.irepository import IRepository


class MongoRepository(IRepository):
    model = Model

    async def get_all(self, sort=None):
        with self.session_factory() as session:
            return await session.find(self.model, sort=sort)

    async def insert_one(self, values: dict):
        entity = self.model(**values)
        with self.session_factory() as session:
            return await session.save(entity)
