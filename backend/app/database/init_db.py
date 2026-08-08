from app.database.base import Base
from app.database.connection import engine
from app.models import User


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("DATABASE TABLES CREATED")