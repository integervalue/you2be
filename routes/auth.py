from flask import render_template, request, redirect, url_for, session
import bcrypt
from utils.db import get_db
from utils.get_all_videos import get_videos
from app import app


@app.route('/')
def index():
    videos = get_videos()
    return render_template('home.html', videos=videos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = get_db()
        #Fetch the user row matching the username entered
        user = db.execute('SELECT * FROM users WHERE username = ?', (request.form['username'],)).fetchone()
        #Checks if such a user exists first, if yes compares the password hashes
        if user is None or not bcrypt.checkpw(request.form['password'].encode('utf-8'), user[2]):
            #if no user is found or the password is wrong, returns error
            return 'Incorrect username or password'
        #Storing the username in session
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        db = get_db()
        #Generate the password hash to be stored in the database
        hashed_password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        db.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',
                   (request.form['username'], hashed_password))
        db.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
