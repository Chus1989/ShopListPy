from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

Base = declarative_base()

class DatabaseConnection:
    def __init__(self, db_folder='DB', db_name='app.db'):
        
        if not os.path.exists(db_folder):
            os.makedirs(db_folder)

        self.database_path = os.path.join(db_folder, db_name)
        self.database_url = f"sqlite:///{self.database_path}"

        self.engine = create_engine(self.database_url, echo=True)
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        
        self._initialize_db()

    def _initialize_db(self):
        
        if not os.path.exists(self.database_path):
            print(f"Base de datos no encontrada. Creándola en {self.database_path}...")
            Base.metadata.create_all(self.engine)
        else:
            print(f"Base de datos encontrada en {self.database_path}. Conexión lista.")
            Base.metadata.create_all(self.engine)

    def get_session(self):
        
        return self.session_local()