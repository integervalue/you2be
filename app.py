from flask import Flask

app = Flask(__name__)
app.secret_key = '$2b$12$lQkWwfuNu49obBjU1T6Rneyayow9Mwf'
app.config['UPLOAD_VIDS_PATH'] = 'static/uploads/videos'
app.config['UPLOAD_THUMBNAILS_PATH'] = 'static/uploads/thumbnails'
app.config['DB_PATH'] = './database/you2be.db'

from routes.auth import *
from routes.videos import *
from routes.reactions import *
from routes.error_handlers import *
from routes.playlists import *

#Initialise the databse if the ".db" file is missing
from database import init_db
init_db.create_database()

#Use when running development server instead of production
# if __name__ == "__main__":
#     app.run(debug=True)