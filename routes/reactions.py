from flask import jsonify, redirect, request, session, url_for
from app import app
from utils.insert_reaction import insert_reaction, remove_reaction, toggle_reaction

@app.route('/like', methods=['GET', 'POST'])
def like_video():
    #Checking whether the user is logged in
    if 'username' in session:
        video_id = request.form['video_id']
        user_id = request.form['user_id']
        
        #When reaction is 1, it means like
        insert_reaction(int(user_id), int(video_id), 1)

        return jsonify({'message': 'Liked successfully'})
    else:
        return redirect(url_for('login'))

@app.route('/dislike', methods=['GET', 'POST'])
def dislike_video():
    if 'username' in session:
        video_id = request.form['video_id']
        user_id = request.form['user_id']

        #When reaction is -1, it means dislike
        insert_reaction(int(user_id), int(video_id), -1)

        return jsonify({'message': 'Disliked successfully'})
    else:
        return redirect(url_for('login'))

@app.route('/remove_reaction', methods=['GET', 'PATCH'])
def remove():
    if 'username' in session:
        video_id = request.form['video_id']
        user_id = request.form['user_id']
        current_reaction = request.form['current_reaction']

        #The current reaction is needed to know how to update the like/dislike counters
        remove_reaction(int(user_id), int(video_id), int(current_reaction))

        return jsonify({'message': 'Removed reaction successfully'})
    else:
        return redirect(url_for('login'))

@app.route('/toggle_reaction', methods=['GET', 'PATCH'])
def reverse():
    if 'username' in session:
        video_id = request.form['video_id']
        user_id = request.form['user_id']
        current_reaction = request.form['current_reaction']

        #The current reaction is needed so that a video marked as liked is toggled to be marked as disliked and vice versa
        toggle_reaction(int(user_id), int(video_id), int(current_reaction))

        return jsonify({'message': 'Toggled reaction successfully'})
    else:
        return redirect(url_for('login'))