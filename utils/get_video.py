from flask import session
from utils.db import get_db
from utils.get_id import get_user_id

def get_video_by_id(video_id):
    db = get_db()
    logged_in_user_id = 0

    video = db.execute('SELECT * FROM videos WHERE id = ?', (video_id,)).fetchone()

    if 'username' in session:
        logged_in_username = session['username']

        logged_in_user_id = get_user_id(logged_in_username)

    if video:
        uploader_username = db.execute('SELECT username FROM users WHERE id = ?', (video[5],)).fetchone()[0]
        reaction = db.execute('SELECT * FROM reactions WHERE user_id = ? AND video_id = ?', (logged_in_user_id, int(video_id),)).fetchone()
        active = reaction[3] if reaction is not None else 0

        # Check if the video is in a playlist belonging to the logged-in user
        in_playlist = db.execute('SELECT COUNT(*) FROM playlist_videos WHERE playlist_id IN (SELECT id FROM playlists WHERE user_id = ?) AND video_id = ?', (logged_in_user_id, int(video_id))).fetchone()[0]

        #For every videos id in playlist, get the video and its data
        video_details = {
            'id': video[0],
            'title': video[1],
            'upload_date': video[2].split(' ', 1)[0],
            'file_path': video[3].split('/', 2)[-1],
            'thumbnail_path': video[4],
            'uploaded_by': video[5],
            'uploader_username': uploader_username,
            'like_counter': video[6],
            'dislike_counter': video[7],
            'reaction_active': active,
            'in_playlist': in_playlist,
            'logged_in_user_id': logged_in_user_id
        }
        return video_details
    else:
        return None
