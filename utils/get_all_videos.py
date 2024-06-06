from utils.db import get_db

def get_videos():
    db = get_db()
    #Select all videos and their data in the database
    videos = db.execute('SELECT id, title, thumbnail_path, uploaded_by FROM videos ORDER BY upload_datetime DESC').fetchall()
    #Preprocessing needed so that the html templates know what's what
    mapped_videos = [{'id': video[0], 'title': video[1], 'thumbnail_path': video[2], 'uploader': db.execute('SELECT username FROM users WHERE id = ?', (video[3],)).fetchone()[0]} for video in videos]

    return mapped_videos