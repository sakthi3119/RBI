from app.models import Base
from app.config import engine

def initialize_database():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

if __name__ == "__main__":
    initialize_database()
