from flask import current_app, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from app import app
import os
from utils.thumbnail_generator import generate_thumbnail
from utils.get_id import get_user_id
from utils.insert_video import insert_vid
from utils.upload_id_generator import genID
from utils.get_video import get_video_by_id
from utils.get_liked_disliked import get_liked_videos, get_disliked_videos
from utils.get_playlists import get_playlist


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    #Checking whether the user is logged in
    if 'username' in session:
        if request.method == 'POST':
            #Randomly generated ID so that if a file has the same name as a previously uploaded file, there is no conflict
            upload_id = genID()
            # Get title the user provided
            title = request.form['title']
            #Get the file itself
            file = request.files['file']

            # Save the video file
            if file:
                # Generate a unique filename
                filename = f"video_{upload_id}_{secure_filename(file.filename)}"
                file_path = os.path.join(current_app.config['UPLOAD_VIDS_PATH'], filename)
                file.save(file_path)

                # Generate thumbnail from the video
                thumbnail_path = generate_thumbnail(file_path)

                # Get the ID of the logged-in user
                user_id = get_user_id(session['username'])

                # Insert the video details into the database
                insert_vid(title, file_path, thumbnail_path, user_id)

                # Redirect to homepage
                return redirect(url_for('index'))

        return render_template('upload.html')
    else:
        return redirect(url_for('login'))

@app.route('/view/<video_id>')
def view(video_id):
    video = get_video_by_id(video_id)
    if video:
        return render_template('view_video.html', video=video)
    else:
        return 'Video not found'

@app.route('/liked_disliked')
def liked_disliked():
    if 'username' in session:
        #Get liked and disliked videos associated with the logged in user (checks for the username in session storage)
        liked_videos = get_liked_videos()
        disliked_videos = get_disliked_videos()
        return render_template('liked_disliked.html', liked_videos=liked_videos, disliked_videos=disliked_videos)
    else:
        return redirect(url_for('login'))
    
@app.route('/view_playlist')
def view_playlist():
    if 'username' in session:
        #Get playlist videos associated with the logged in user (checks for the username in session storage)
        playlist = get_playlist()

        return render_template('playlists.html', playlist=playlist)
    else:
        return redirect(url_for('login'))