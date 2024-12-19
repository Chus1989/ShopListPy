from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

Base = declarative_base()
'''
JESUS JOYAS 2024 shop list
This class create a instance of a DB and generates the engine with sqlalchemy to 
operate with it
'''
class DatabaseConnection:

    '''
    This init get the path, and initialize de database with this engine
    args:
        db_folder:String: The folder of the database
        db_name:String: The name of the database
    '''
    def __init__(self, db_folder='DB', db_name='app.db'):
        
        if not os.path.exists(db_folder):
            os.makedirs(db_folder)

        self.database_path = os.path.join(db_folder, db_name)
        self.database_url = f"sqlite:///{self.database_path}"

        self.engine = create_engine(self.database_url, echo=True)
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        
        self._initialize_db()

    '''
    This method create the database if not exists or initialize the datbase 
    with the base of the tables iof the model
    '''
    def _initialize_db(self):
        
        if not os.path.exists(self.database_path):
            print(f"Base de datos no encontrada. Creándola en {self.database_path}...")
            Base.metadata.create_all(self.engine)
        else:
            print(f"Base de datos encontrada en {self.database_path}. Conexión lista.")
            Base.metadata.create_all(self.engine)
    '''
    This method get the actual session of the database. 
    Return: The session of the database in local
    '''
    def get_session(self):
        
        return self.session_local()