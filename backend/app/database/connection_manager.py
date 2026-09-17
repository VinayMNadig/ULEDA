from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from app.database.active_database import active_database


class ConnectionManager:

    def __init__(self):
        self.engine = None
        self.SessionLocal = None
        self.database_type = None

    # ======================================
    # SQLite
    # ======================================

    def connect_sqlite(self, db_path: str):

        try:

            print("=" * 60)
            print("CONNECTING SQLITE DATABASE")
            print("Database Path :", db_path)

            url = f"sqlite:///{db_path}"

            self.engine = create_engine(
                url,
                connect_args={"check_same_thread": False}
            )

            self.SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
            )

            self.database_type = "SQLite"

            active_database.set_database(
                db_path,
                "SQLite"
            )

            print("Engine :", self.engine)
            print("SQLite Connected Successfully")
            print("=" * 60)

            return True

        except Exception as e:
            print(e)
            raise Exception(str(e))

    # ======================================
    # MySQL
    # ======================================

    def connect_mysql(
        self,
        host,
        port,
        username,
        password,
        database
    ):

        url = (
            f"mysql+pymysql://"
            f"{username}:{password}"
            f"@{host}:{port}/{database}"
        )

        self.engine = create_engine(url)

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False
        )

        self.database_type = "MySQL"

        active_database.set_database(
            database,
            "MySQL"
        )

    # ======================================
    # PostgreSQL
    # ======================================

    def connect_postgresql(
        self,
        host,
        port,
        username,
        password,
        database
    ):

        url = (
            f"postgresql+psycopg2://"
            f"{username}:{password}"
            f"@{host}:{port}/{database}"
        )

        self.engine = create_engine(url)

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False
        )

        self.database_type = "PostgreSQL"

        active_database.set_database(
            database,
            "PostgreSQL"
        )

    # ======================================
    # Oracle
    # ======================================

    def connect_oracle(
        self,
        host,
        port,
        username,
        password,
        service_name
    ):

        url = (
            f"oracle+oracledb://"
            f"{username}:{password}"
            f"@{host}:{port}/?service_name={service_name}"
        )

        self.engine = create_engine(url)

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False
        )

        self.database_type = "Oracle"

        active_database.set_database(
            service_name,
            "Oracle"
        )

    # ======================================
    # SQL Server
    # ======================================

    def connect_sqlserver(
        self,
        host,
        port,
        username,
        password,
        database
    ):

        url = (
            "mssql+pyodbc://"
            f"{username}:{password}"
            f"@{host}:{port}/{database}"
            "?driver=ODBC+Driver+17+for+SQL+Server"
        )

        self.engine = create_engine(url)

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False
        )

        self.database_type = "SQL Server"

        active_database.set_database(
            database,
            "SQL Server"
        )

    # ======================================
    # Session
    # ======================================

    def get_session(self):

        if self.SessionLocal is None:
            raise Exception("No database connected.")

        return self.SessionLocal()

    # ======================================
    # Test Connection
    # ======================================

    def test_connection(self):

        if self.engine is None:
            return False

        try:
            with self.engine.connect() as conn:
                conn.exec_driver_sql("SELECT 1")

            return True

        except SQLAlchemyError:
            return False

    # ======================================
    # Disconnect
    # ======================================

    def disconnect(self):

        if self.engine:
            self.engine.dispose()

        self.engine = None
        self.SessionLocal = None
        self.database_type = None

        active_database.clear()

    # ======================================
    # Status
    # ======================================

    def status(self):

        return {
            "connected": self.engine is not None,
            "database_type": self.database_type,
            "active_database": active_database.summary()
        }


connection_manager = ConnectionManager()