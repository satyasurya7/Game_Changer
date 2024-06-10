from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi.exceptions import HTTPException
from typing import List

app = FastAPI()

# origins = ["*"]  # Update with specific origins if needed
origins = ["https://www.gamechangerofficial.com", "app.gc.clever-flower-19874.pktriot.net"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# PostgreSQL connection details
DATABASE_URL = "postgresql://postgres:postgres@localhost/gamechanger"

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

class Feedback(BaseModel):
    name: str
    subject: str
    feedback: str


@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    try:
        print("Feedback received:", feedback)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (name, subject, feedback) VALUES (%s, %s, %s)", 
                       (feedback.name, feedback.subject, feedback.feedback))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Feedback submitted successfully"}
    except Exception as e:
        print(f"Error creating feedback: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/feedback", response_model=List[Feedback])
async def read_feedback():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, subject, feedback FROM feedback")
        feedbacks = cursor.fetchall()
        cursor.close()
        conn.close()
        return feedbacks
    except Exception as e:
        print(f"Error fetching feedback: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def read_index():
    return FileResponse('static/index.html')
