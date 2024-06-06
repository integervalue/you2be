from flask import session
from utils.db import get_db
from utils.get_id import get_user_id

def get_playlist():
    db = get_db()

    #Get the logged in user's username from session storage
    username = session['username']

    #Get the user id
    user_id = get_user_id(username)

    #Get a playlist id associated with a user id
    playlist_row = db.execute('SELECT id FROM playlists WHERE user_id = ?', (user_id,)).fetchone()

    #Check if a playlist was found
    playlist_id = playlist_row[0] if playlist_row is not None else None

    #Playlists and playlist content are stored in two different tables
    #Get the videos inside the playlist
    playlist_videos = db.execute('SELECT video_id FROM playlist_videos WHERE playlist_id = ?', (playlist_id,)).fetchall()

    mapped_playlist_videos = []
    #For every videos id in playlist, get the video and its data
    for pl_video in playlist_videos:
        video = db.execute('SELECT id, title, upload_datetime, thumbnail_path, uploaded_by, like_counter, dislike_counter FROM videos WHERE id=?', (pl_video[0],)).fetchone()
        
        #Preprocessing needed so that the html templates know what's what
        mapped_video = {
            'id': video[0], 
            'title': video[1], 
            'upload_date': video[2].split(' ', 1)[0], 
            'thumbnail_path': video[3], 
            'uploader_username': db.execute('SELECT username FROM users WHERE id = ?', (video[4],)).fetchone()[0],
            'like_counter': video[5], 
            'dislike_counter': video[6]
        }
        mapped_playlist_videos.append(mapped_video)

    return mapped_playlist_videos

def add_to_pl(userId, videoId):
    db = get_db()
    #Check whether there is a playlist associated with the user
    playlist_id = db.execute('SELECT id FROM playlists WHERE user_id = ?', (userId,)).fetchone()

    if playlist_id is not None:
        #A playlist exists, add the video to it
        db.execute('INSERT INTO playlist_videos (playlist_id, video_id) VALUES (?, ?)', (playlist_id[0], videoId))
    else:
        #Create a new playlist
        db.execute('INSERT INTO playlists (name, user_id) VALUES (?, ?);', ("playlist", userId))
        #Get the ID of the new plylist
        playlist_id = db.execute('SELECT id FROM playlists WHERE user_id = ?', (userId,)).fetchone()
        #Actually insert the video into the playlist
        db.execute('INSERT INTO playlist_videos (playlist_id, video_id) VALUES (?, ?)', (playlist_id[0], videoId))
        
        
    db.commit()
    db.close()

def remove_from_pl(userId, videoId):
    db = get_db()
    
    #Get the playlist id associated with the user
    playlist_id = db.execute('SELECT id FROM playlists WHERE user_id = ?', (userId,)).fetchone()

    #Delete the video from the playlist
    db.execute('DELETE FROM playlist_videos WHERE playlist_id = ? AND video_id = ?', (playlist_id[0], videoId))
    
    db.commit()
    db.close()