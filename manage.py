from models import db, User
from server import app

@app.shell_context_processor
def shell_context_processor():
    return dict(
        db=db, User=User, app=app
    )