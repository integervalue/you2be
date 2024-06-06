from utils.db import get_db

#Get the user id associated with a username
def get_user_id(username):
    db = get_db()
    user_id = db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()[0]

    return user_id