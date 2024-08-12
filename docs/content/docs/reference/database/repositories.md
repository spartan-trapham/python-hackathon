+++
weight = 3203
date = "2023-05-03T22:37:22+01:00"
draft = false
author = "Pham Xuan Tra"
title = "Repositories"
icon = "rocket_launch"
toc = true
description = "Repository description"
publishdate = "2023-05-03T22:37:22+01:00"
tags = ["intermediate"]
+++

Repository is a layer of logic supporting services interact with data store. Usually, repository is used to interact with database. In form of SQLAlchemy there are 2 types of building a repository method: [ORM](#repository-using-orm) and [Core](#repository-using-core). Both these techniques follow same design pattern that services will manage the connection (in core) and session (in orm). All repositories will receive the the connections or sessions from services before executing their logic to database. This pattern gives some benefit:
- Service will decide what the next step (retry, skip or rollback) if the queries/mutations in the repository go wrong.
- The connections and transactions is managed from services without caring about number of queries in repositories.

Both connections and sessions are managed by connection pool in the SQLAlchemy instance at configuring time.
```python
class Database:
    def __init__(self, config: DatabaseConfig) -> None:
        self.url = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{name}".format_map(config.dict())
        self._engine = create_engine(
            self.url,
            max_overflow=config.overflow_connections,
            pool_size=config.max_connections,
        )

        self._metadata = MetaData()
        self._metadata.bind = self._engine
        self._session = scoped_session(
            sessionmaker(
                autocommit=False,
                expire_on_commit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )
        logger.info("Finish initialization database")
```

### Repository using Core

1. Open connection from service
```python
def remove(self, user_id: uuid.UUID) -> None:
    with self.db.connect() as connect:
        await self.user_repo.soft_delete(connect, user_id)
```
2. Execute query with connection passed from service
```python
async def soft_delete(self, connection: Connection, user_id: uuid.UUID):
    stmt = (
        update(User.__table__)
        .where(User.c.id == user_id)
        .values(deleted_at=datetime.datetime.utcnow())
    )
    return await connection.execute(stmt)
```
The connection must be passed to all other repository methods using Core so that all queries will use the same connection instead of creating new ones.

### Repository using ORM

1. Open session from service
```python
async def by_id(self, user_id: uuid.UUID) -> User:
    user: User
    with self.db.session() as session:
        user = await self.user_repo.by_id(session, user_id)
    return user
```
2. Execute query with connection passed from service
```python
async def by_id(self, session: Session, user_id: uuid.UUID):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise AppException(USER_NOT_FOUND)
    return user
```
The session must be passed to all other repository methods using ORM so that all queries will use the same connection and transaction instead of creating new ones.

