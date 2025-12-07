import json
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), default='General', index=True)
    question = db.Column(db.Text, nullable=False)
    choices = db.Column(db.Text, nullable=False)  # stored as JSON list
    correct_index = db.Column(db.Integer, nullable=False)

    def choices_list(self):
        return json.loads(self.choices)
