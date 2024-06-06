from flask import render_template
from app import app

#Page not found error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal server error (server side error)
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500