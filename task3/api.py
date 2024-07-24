from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/query")
def query(query: str):
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required")
    return {"message": f"Query received: {query}"}