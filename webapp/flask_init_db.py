## Script to initialize the flask db if it does not exist.

from flaskr import db
import os.path

def flask_init_db():
    if not os.path.exists('instance/flaskr.sqlite'):
        db.init_db_command()

if __name__ == "__main__":
    flask_init_db()
