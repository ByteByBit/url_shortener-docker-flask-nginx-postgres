import os
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    redirect,
    url_for,
    render_template
)
from flask_sqlalchemy import SQLAlchemy

from project.models import InsertURL, Shortener_Form


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


@app.route("/shortener", methods=["GET", "POST"])
def shortener():
    '''
    Shortener service.
    [GET] -> Shortener form.
    [POST] -> Shorten the URL submitted with the form.
    '''

    # POST form.
    if request.method == "POST":

        url = request.form.get('url')

        # Submitted URL is empty.
        if not url:
            return render_template('error.html')

        insert = InsertURL()
        id = insert.insert(url)

        if id == -1:
            return render_template('error.html')

        new_url = insert.result(id)
        
        return render_template('success.html', new_url=new_url)

    form = Shortener_Form()
    return render_template('shortener.html', form=form)
