from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB = "database.db"

# Initialize DB
def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                project TEXT NOT NULL,
                hours REAL NOT NULL,
                points INTEGER NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    project = request.form['project']
    hours = float(request.form['hours'])
    points = int(hours * 10)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(DB) as conn:
        conn.execute('''
            INSERT INTO submissions (username, project, hours, points, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, project, hours, points, timestamp))

    return redirect(url_for('leaderboard'))

@app.route('/leaderboard')
def leaderboard():
    with sqlite3.connect(DB) as conn:
        cursor = conn.execute('''
            SELECT username, SUM(points) as total_points
            FROM submissions
            GROUP BY username
            ORDER BY total_points DESC
            LIMIT 10
        ''')
        leaders = cursor.fetchall()
    return render_template('leaderboard.html', leaders=leaders)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
