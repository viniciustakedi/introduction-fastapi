from h11 import Data
import sqlalchemy
from config import DATABASE_URL, metadata
from Models.user_model import UserModel as User

def migrate_db(database_url = DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)

if __name__ == "__main__":
    migrate_db()