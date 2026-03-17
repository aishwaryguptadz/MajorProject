import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=ANUSH\SQLEXPRESS;"
        "DATABASE=MarineAI;"
        "Trusted_Connection=yes;"
    )
    return conn

print(pyodbc.drivers())
