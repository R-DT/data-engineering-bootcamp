from contextlib import contextmanager
from os import environ
from typing import Generator
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv 
from src.logger import setup_logger

logger = setup_logger(__name__)

# Force populate your runtime dictionary memory from the local .env file profile
load_dotenv()

class DatabaseConnector:
    """Manages secure connection pooling and safe transactions into PostgreSQL."""
    
    def __init__(self) -> None:
        # Load environment variables explicitly
        db_user = environ.get("DB_USER", "postgres")
        db_pass = environ.get("DB_PASS", "your_secure_password_here")
        db_host = environ.get("DB_HOST", "localhost")
        db_port = environ.get("DB_PORT", "5432")
        db_name = environ.get("DB_NAME", "fintech_db")
        
        # Diagnostic print to check environment variable resolution
        logger.info(f"DIAGNOSTIC - Loaded DB_PASS string length: {len(db_pass)} characters.")
        logger.info(f"DIAGNOSTIC - Loaded DB_HOST target string: '{db_host}' on port: '{db_port}'")
        
        self.connection_url = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        self.engine = create_engine(
            self.connection_url, 
            pool_size=10, 
            max_overflow=20,
            pool_pre_ping=True
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            
    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        """Context manager to ensure transactions are safely committed or rolled back."""
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error("Database Transaction Failure: Issuing rollback command.")
            raise e
        finally:
            session.close()

    def test_connection(self) -> bool:
        """Executes a diagnostic verification handshake against the warehouse."""
        try:
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            logger.info("Database Connection: Live and responding successfully.")
            return True
        except Exception as e:
            logger.error(f"Database Handshake Failed: {str(e)}")
            return False
