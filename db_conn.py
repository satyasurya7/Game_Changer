import psycopg2

DATABASE_URL = "postgresql://postgres:postgres@localhost/gamechanger"

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


def create_feedback(name, subject, feedback):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (name, subject, feedback) VALUES (%s, %s, %s)", 
                   (name, subject, feedback))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Feedback submitted successfully"}

create_feedback("John Doe", "Test", "This is a test message")
