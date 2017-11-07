import logging

from flask import Flask

# This defines a Flask application
app = Flask(__name__)


# Magical annotations define URL routing via the Flask application
@app.route('/')
def hello():
    return 'Hello World!'


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


# This allows you to run locally.
# When run in GCP, Gunicorn is used instead (see entrypoint in app.yaml) to
# Access the Flack app via WSGI
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
