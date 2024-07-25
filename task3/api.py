from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

from pydantic import BaseModel, Field

mocked_db = {
    "query1": {"query": "How do I reset my device to factory settings?", "answer": "To reset your device to factory settings, go to 'Settings' > 'System' > 'Reset' > 'Factory data reset'. Confirm the reset by following the on-screen instructions. Please note that this will erase all data on the device."},
    "query2": {"query": "What should I do if my device won't turn on?", "answer": "If your device won't turn on, try the following steps: \n   - Ensure the device is charged by connecting it to the charger for at least 30 minutes. \n   - Press and hold the power button for 10-15 seconds to force a restart. \n   - If the device still does not turn on, try using a different charger or cable. \n   - If none of these steps work, please contact customer support for further assistance."},
}

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Schema for the query
class QueryBase(BaseModel):
    query: str

class Query(QueryBase):
    query: str 
    answer: str 

#Model for the query
class QueryModel(Base):
    __tablename__ = "query"

    query = Column(String, primary_key=True)
    answer = Column(String, index=True)

app = FastAPI()

def get_query(db: Session, query: str):
    return db.query(QueryModel).filter(QueryModel.query == query).first()

@app.get("/query")
def query(query: str):
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required")
    return {"message": f"Query received: {query}"}

@app.get("/query/{query}", response_model=Query)
def get_mocked_query(query: str):
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required")
    if query not in mocked_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return mocked_db[query]

@app.get("/query/sql/{query}", response_model=Query)
def get_sql_query(query: str, db: Session = Depends(get_db)):
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required")
    db_query = get_query(db, query=query)
    if db_query is None:
        raise HTTPException(status_code=404, detail="No result")
    return db_query