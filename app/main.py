from fastapi import FastAPI
import uvicorn
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from sqlalchemy.sql import text
from app.db.base import Base
from app.db.session import engine



app = FastAPI()


Base.metadata.create_all(bind=engine)



@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "message": "Database connection is healthy."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
