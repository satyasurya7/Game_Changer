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
    print("Entered create_feedback")
    try:
        print("Entered create_feedback")
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
        raise e


@app.get("/feed")
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
