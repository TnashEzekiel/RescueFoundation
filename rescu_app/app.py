"""
description: Application description here

@author: Judith Nyatsine<@gmail.com>
@date: 01-June-2017

"""

from flask import Flask
from flask import render_template
from flask import request
from flask import flash

from rescu.rescu import *

import time

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.debug = True

@app.route("/")
def index():
	return render_template("ContactUs.html")


@app.route("/contact-us", methods=['POST', 'GET'])
def contact_us():

    # process user supplied form data.
    if request.method == "POST":
        full_name = request.form['full_name']
        phone_number = request.form['phone_number'] 
        email_address = request.form['email_address']
        message = request.form['message']

        # insert data into database
        create_contact_message(full_name, phone_number, email_address, message)

        # flash(request, '')

    return render_template('ContactUs.html')


@app.route("/contact-messages", methods=['POST', 'GET'])
def contact_messages():

    messages = retrieve_messages()

    return render_template('messages-list.html', messages=messages)


if __name__ == "__main__":

    init_db()

    app.run()


