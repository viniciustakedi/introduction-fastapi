import databases
import sqlalchemy
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
DATABASE_IS_DEVELOP = os.getenv('DATABASE_IS_DEVELOP', 'false') in ('true', 'yes')
database = databases.Database(DATABASE_URL, force_rollback=DATABASE_IS_DEVELOP)
metadata = sqlalchemy.MetaData()