# Quiz Master (Cybersecurity Quiz)

Simple Flask-based quiz application focused on cybersecurity topics.

Quick start (Windows PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
python run_db.py
$env:FLASK_APP = "quiz_master.app"
flask run --port 5000
```

- Open http://127.0.0.1:5000/ to browse categories and take quizzes.
- Admin UI at `/admin` lets you add questions (4 choice inputs, 0-based correct index).

Project layout:
- `quiz_master/` - app package
- `run_db.py` - initialize SQLite DB and seed sample questions
- `requirements.txt` - Python dependencies

Next steps:
- Add user accounts, timed quizzes, leaderboards
- Improve admin UI and validation
