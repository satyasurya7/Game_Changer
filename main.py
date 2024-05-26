from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# PostgreSQL connection details
DATABASE_URL = "postgresql://user:password@localhost:5432/feedback"

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

class Feedback(BaseModel):
    email: str
    message: str

@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (email, message) VALUES (%s, %s)", 
                   (feedback.email, feedback.message))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Feedback submitted successfully"}

@app.get("/feedback")
async def read_feedback():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    feedbacks = cursor.fetchall()
    cursor.close()
    conn.close()
    return feedbacks

@app.get("/", response_class=HTMLResponse)
async def read_index():
    return FileResponse('static/index.html')
