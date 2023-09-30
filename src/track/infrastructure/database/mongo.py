from contextlib import contextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine


class MongoDatabase():
    def __init__(self, database: str, host: str, port: str, user: str, password: str, authentication_source: str,
                 use_connection_string: bool, connection_string: str) -> None:
        self.database = database
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.authentication_source = authentication_source
        self.use_connection_string = use_connection_string

        if use_connection_string:
            mongo_connection = connection_string
        elif self.user and self.password:
            mongo_connection = f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?authSource={self.authentication_source}'
        else:
            mongo_connection = f'mongodb://{self.host}:{self.port}'

        self.motor_client = AsyncIOMotorClient(mongo_connection)

        if self.database:
            self._session_factory = AIOEngine(client=self.motor_client, database=self.database)
        else:
            self._session_factory = AIOEngine(client=self.motor_client)

    @contextmanager
    def session(self):
        session = self._session_factory
        try:
            yield session
        except Exception:
            raise
