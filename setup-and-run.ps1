python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --no-cache-dir -r requirements.txt
python manage.py runserver 0.0.0.0:8000