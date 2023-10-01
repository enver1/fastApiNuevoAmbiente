
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DB_DIALECT = 'mysql+pymysql'
DB_USER = 'eflores'
DB_PASSWORD = 'Pichincha1'
DB_HOST = '192.168.80.73:3306'
DB_NAME = 'nuevoambiente'
URL_CONNECTION = '{}://{}:{}@{}/{}'.format(DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
engine = create_engine(URL_CONNECTION)
#engine = create_engine("mysql+pymysql://danilo:1234@localhost:3306/cursos")
localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()