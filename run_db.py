from quiz_master.models import db, Question
from quiz_master.app import create_app
import json

SAMPLE_QUESTIONS = [
    {
        'category': 'Web',
        'question': 'Which HTTP header is used to prevent clickjacking by specifying allowed framing origins?',
        'choices': ['Content-Security-Policy', 'X-Frame-Options', 'Strict-Transport-Security', 'X-Content-Type-Options'],
        'correct_index': 1
    },
    {
        'category': 'Cryptography',
        'question': 'Which property ensures that a hash function is hard to invert?',
        'choices': ['Collision resistance', 'Preimage resistance', 'Avalanche effect', 'Determinism'],
        'correct_index': 1
    },
    {
        'category': 'Network',
        'question': 'What is the primary purpose of a firewall?',
        'choices': ['Encrypt traffic', 'Filter/inspect traffic', 'Store logs', 'Authenticate users'],
        'correct_index': 1
    },
    {
        'category': 'General',
        'question': 'Which principle says a user should have only the minimum privileges necessary?',
        'choices': ['Fail-safe defaults', 'Least privilege', 'Defense in depth', 'Separation of duties'],
        'correct_index': 1
    },
    {
        'category': 'Web',
        'question': 'Which vulnerability allows an attacker to inject and execute scripts in a victim browser?',
        'choices': ['SQL Injection', 'CSRF', 'XSS', 'Directory Traversal'],
        'correct_index': 2
    }
]


def init_db():
    app = create_app()
    with app.app_context():
        db.create_all()
        if Question.query.count() == 0:
            for s in SAMPLE_QUESTIONS:
                q = Question(category=s['category'], question=s['question'], choices=json.dumps(s['choices']), correct_index=s['correct_index'])
                db.session.add(q)
            db.session.commit()
            print('Seeded sample questions.')
        else:
            print('Database already initialized.')


if __name__ == '__main__':
    init_db()
