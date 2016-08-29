import logging

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# toolbar = DebugToolbarExtension(app)

@app.route('/notify_me', methods=['POST'])
def notify_me():
    try:
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        logging.info('First: %s, Last: %s, Email: %s' % (firstName, lastName, email))
        return 'Thanks!', 200
    except:
        logging.exception('Invalid incoming form: %s' % request.form)
        return 'Error parsing form', 500
    
"""
# [START form]
@app.route('/form')
def form():
   return render_template('form.html')
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
    # [END render_template]
"""

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
