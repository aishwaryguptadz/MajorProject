## Backend Setup (FastAPI)

1. Clone the repository

git clone https://github.com/aishwaryguptadz/MajorProject.git
cd MajorProject/Backend-API

2. Install dependencies

pip install -r requirements.txt

3. Configure database

Create a .env file:

DB_SERVER=ANUSH\SQLEXPRESS
DB_NAME=MarineAI
DB_DRIVER=SQL Server

4. Run API server

uvicorn app:app --reload --host 0.0.0.0 --port 8000

5. Test APIs

Open:
http://localhost:8000/docs
