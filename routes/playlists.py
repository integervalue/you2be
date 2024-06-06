from flask import jsonify, redirect, request, session, url_for
from app import app
from utils.get_playlists import add_to_pl, remove_from_pl


@app.route('/add_to_playlist', methods=['POST'])
def add_to_playlist():
    #Check if a username is stored in session, if yes get user_id and video_id and add video to playlist
    if 'username' in session:
        user_id = request.form['user_id']
        video_id = request.form['video_id']

        add_to_pl(user_id, video_id)

        return jsonify({'message': 'Added to playlist successfully'})
    else:
        return redirect(url_for('login'))
    
@app.route('/remove_from_playlist', methods=['POST'])
def remove_from_playlist():
    #Check if a username is stored in session, if yes get user_id and video_id and remove video from playlist
    if 'username' in session:
        user_id = request.form['user_id']
        video_id = request.form['video_id']

        remove_from_pl(user_id, video_id)

        return jsonify({'message': 'Removed from playlist successfully'})
    else:
        return redirect(url_for('login'))