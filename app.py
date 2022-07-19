import string
import time
import pyodbc
import os
from flask import Flask, Request, render_template, request, flash

app = Flask(__name__, template_folder="templates")

connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:adbsai.database.windows.net,1433;Database=adb;Uid=sainath;Pwd=Shiro@2018;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30')

cursor = connection.cursor()



@app.route('/', methods=['POST', 'GET'])
def Hello():
    return render_template('index.html')



if __name__ == '__main__':    
    app.run()

