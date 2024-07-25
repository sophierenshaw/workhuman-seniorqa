from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .api import app, get_db, Base

#SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

#Test for valid query parameter
def test_query_with_valid_input():
    response = client.get("/query?query=Hello")
    assert response.status_code == 200
    assert response.json() == {"message": f"Query received: Hello"}

#Test for valid query parameter with mocked database
def test_query_with_valid_input_mocked_db():    
    response = client.get("/query/How do I reset my device to factory settings?")
    data = response.json()
    assert response.status_code == 200
    assert data["answer"] == "To reset your device to factory settings, go to 'Settings' > 'System' > 'Reset' > 'Factory data reset'. Confirm the reset by following the on-screen instructions. Please note that this will erase all data on the device."

#Test for valid query parameter with sqlite database
def test_query_with_valid_input_sql_db():    
    response = client.get("/query/db/How do I reset my device to factory settings?")
    data = response.json()
    assert response.status_code == 200
    assert data["answer"] == "To reset your device to factory settings, go to 'Settings' > 'System' > 'Reset' > 'Factory data reset'. Confirm the reset by following the on-screen instructions. Please note that this will erase all data on the device."

#Test for no query parameter
def test_query_with_empty_input():
    response = client.get("/query?query=")
    assert response.status_code == 400
    assert response.json() == {"detail": "Query parameter is required"}

#Test for query parameter not provided
def test_query_without_input():
    response = client.get("/query")
    assert response.status_code == 422