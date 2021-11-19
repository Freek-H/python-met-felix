from flask import Flask
from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()
DATABASE_LOGIN = {
    'NAME': os.environ.get('AZURE_NAME'),
    'USER': os.environ.get('AZURE_USER'),
    'PASSWORD': os.environ.get('AZURE_PASSWORD'),
    'HOST': os.environ.get('AZURE_HOST')
}

app = Flask(__name__)

cnxn = pyodbc.connect(f'''
    DRIVER={{ODBC Driver 17 for SQL Server}};
    SERVER={DATABASE_LOGIN['HOST']};
    DATABASE={DATABASE_LOGIN['NAME']};
    UID={DATABASE_LOGIN['USER']};
    PWD={DATABASE_LOGIN['PASSWORD']}''')

cur = cnxn.cursor()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/get/')
def get_test():
    cur.execute('SELECT * FROM [dbo].[test]')
    return f"{cur.fetchall()}"

@app.route("/insert/<s>")
def insert_test(s):
    cur.execute("""
        INSERT INTO [dbo].[test]
        VALUES
            (?)
    """, s)
    cur.execute(f'SELECT * FROM [dbo].[test] WHERE [Name] = ?', s)
    return f"{cur.fetchall()}"

if __name__ == '__main__':
    app.run()
    