from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Draft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(128), nullable=False)  # Firebase UID
    content = db.Column(db.Text, nullable=False)

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()