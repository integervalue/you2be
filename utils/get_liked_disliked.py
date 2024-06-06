from flask import session
from utils.db import get_db
from utils.get_id import get_user_id

def get_liked_videos():
    db = get_db()

    #Get the logged in user's username from session storage
    username = session['username']

    #Get the user id
    user_id = get_user_id(username)

    #Get all the reactions associated with the user id (get the video id on which a reaction was placed)
    likes = db.execute('SELECT video_id FROM reactions WHERE user_id=? AND reaction=1', (user_id,)).fetchall()

    liked_videos = []
    #For every videos id in reactions, get the video and its data
    for like in likes:
        video = db.execute('SELECT id, title, upload_datetime, thumbnail_path, uploaded_by, like_counter, dislike_counter FROM videos WHERE id=?', (like[0],)).fetchone()
        
        #Preprocessing needed so that the html templates know what's what
        mapped_video = {
            'id': video[0], 
            'title': video[1], 
            'upload_date': video[2].split(' ', 1)[0], 
            'thumbnail_path': video[3], 
            'uploaded_by': db.execute('SELECT username FROM users WHERE id = ?', (video[4],)).fetchone()[0], 
            'like_counter': video[5], 
            'dislike_counter': video[6]
        }
        liked_videos.append(mapped_video)

    return liked_videos

def get_disliked_videos():
    db = get_db()

    #Get the logged in user's username from session storage
    username = session['username']

    #Get the user id
    user_id = get_user_id(username)

    #Get all the reactions associated with the user id (get the video id on which a reaction was placed)
    dislikes = db.execute('SELECT video_id FROM reactions WHERE user_id=? AND reaction=-1', (user_id,)).fetchall()

    disliked_videos = []
    #For every videos id in reactions, get the video and its data
    for dislike in dislikes:
        video = db.execute('SELECT id, title, upload_datetime, thumbnail_path, uploaded_by, like_counter, dislike_counter FROM videos WHERE id=?', (dislike[0],)).fetchone()
        
        #Preprocessing needed so that the html templates know what's what
        mapped_video = {
            'id': video[0], 
            'title': video[1], 
            'upload_date': video[2].split(' ', 1)[0], 
            'thumbnail_path': video[3], 
            'uploaded_by': db.execute('SELECT username FROM users WHERE id = ?', (video[4],)).fetchone()[0], 
            'like_counter': video[5], 
            'dislike_counter': video[6]
        }
        disliked_videos.append(mapped_video)

    return disliked_videos
