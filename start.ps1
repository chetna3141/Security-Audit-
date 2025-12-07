# start.ps1 — Setup and run Quiz Master (PowerShell)
# Usage: Open PowerShell, cd to project folder, then run:
#   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#   .\start.ps1

Write-Host "Starting Quiz Master setup..." -ForegroundColor Cyan

# 1) Check python
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) {
    $py = Get-Command py -ErrorAction SilentlyContinue
}
if (-not $py) {
    Write-Host "Python not found. Please install Python and re-run this script." -ForegroundColor Red
    exit 1
}

# 2) Create virtual environment if missing
if (-not (Test-Path .\venv)) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
} else {
    Write-Host "Virtual environment already exists." -ForegroundColor Yellow
}

# 3) Activate virtualenv in this session
Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate.ps1

# 4) Upgrade pip and install requirements
Write-Host "Upgrading pip and installing requirements..."
python -m pip install --upgrade pip
pip install -r .\requirements.txt

# 5) Initialize DB and seed sample questions
Write-Host "Initializing database and seeding sample questions..."
python .\run_db.py

# 6) Start Flask app
Write-Host "Starting Flask development server on http://127.0.0.1:5000" -ForegroundColor Green
$env:FLASK_APP = "quiz_master.app"
python -m flask run --port 5000

# Note: The script will keep running while Flask server is active. Press Ctrl+C to stop.
