# you2be
Python implementation of a video sharing web-app similar to youtube


# Flask:

Create virtualenv:
virtualenv *Name*

Activate(de) virtual env:
source *Name*/bin/activate   —  (deactivate)


# Run web app (development):

* You will need to uncomment the last two lines in app.py

export FLASK_APP=hello.py

export FLASK_ENV=development 

python3 -m flask run --host=0.0.0.0 --port=3000



# Run WSGI server (production):

* Works out of the box

gunicorn wsgi:app --bind 0.0.0.0:3000
