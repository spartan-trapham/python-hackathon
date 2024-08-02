from sqlalchemy import create_engine, text

class DBConection:
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)

    def setup(self) -> None:
        self.connection = self.engine.connect()

    def start(self):
        result = self.connection.execute(text("SELECT version()"))
        return result


    def stop(self):
        self.connection.close()

if __name__ == "__main__":
    connection_string = 'postgresql+psycopg2://postgres:postgres@localhost:54321/postgres'
    dbConn = DBConection(connection_string)
    dbConn.setup()
    result = dbConn.start()
    for row in result:
        print(f"PostgreSQL version: {row[0]}")
    dbConn.stop()
