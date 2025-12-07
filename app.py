import json
from flask import Flask, render_template, request, jsonify, redirect, url_for
from .models import db, Question


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/')
    def index():
        cats = db.session.query(Question.category).distinct().all()
        categories = [c[0] for c in cats]
        return render_template('index.html', categories=categories)

    @app.route('/quiz/<category>')
    def quiz(category):
        qs = Question.query.filter_by(category=category).all()
        return render_template('quiz.html', questions=qs, category=category)

    @app.route('/submit', methods=['POST'])
    def submit():
        data = request.get_json() or {}
        answers = data.get('answers', {})
        score = 0
        total = 0
        results = []
        for qid, sel in answers.items():
            q = Question.query.get(int(qid))
            if not q:
                continue
            total += 1
            correct = q.correct_index
            is_correct = (int(sel) == correct)
            if is_correct:
                score += 1
            results.append({'id': q.id, 'correct': is_correct, 'correct_index': correct})
        return jsonify({'score': score, 'total': total, 'results': results})

    @app.route('/admin')
    def admin():
        qs = Question.query.order_by(Question.id).all()
        return render_template('admin.html', questions=qs)

    @app.route('/admin/add', methods=['POST'])
    def add_question():
        form = request.form
        choices = [c for c in form.getlist('choices') if c.strip()]
        q = Question(
            question=form.get('question',''),
            category=form.get('category','General'),
            choices=json.dumps(choices),
            correct_index=int(form.get('correct_index',0))
        )
        db.session.add(q)
        db.session.commit()
        return redirect(url_for('admin'))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
