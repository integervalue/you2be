from utils.db import get_db
from datetime import datetime

def insert_vid(title, file_path, thumbnail_path, uploaded_by):
    # Connect to the database
    db = get_db()

    # Get the current datetime
    upload_datetime = datetime.now()

    # Insert the video details into the table
    db.execute("""
        INSERT INTO videos (title, upload_datetime, file_path, thumbnail_path, uploaded_by)
        VALUES (?, ?, ?, ?, ?)
    """, (title, upload_datetime, file_path, thumbnail_path, uploaded_by))


    # Commit the changes and close the connection
    db.commit()
    db.close()
