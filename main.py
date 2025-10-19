from flask import Flask, render_template, request, redirect
from datetime import datetime
positionInLine=350
app = Flask(__name__)
leaderboard = []
@app.route("/")
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def username():
    
    Name=request.form["username"]
    Class=request.form["Class"]
    asignmentName=request.form["asignmentName"]
    submission = {
        'name': Name,
        'class': Class,
        'asignment':asignmentName,
        'time': datetime.now()
    }
    leaderboard.append(submission)
    leaderboard.sort(key=lambda x: x['time'])
    return redirect('/leaderboard')
@app.route('/leaderboard')
def show_leaderboard():
    return render_template('leaderboard.html', leaderboard=leaderboard)
def show_asignments():
    return render_template('asignments.html')
def show_flashcards():
    return render_template('flashcards.html')
if __name__ == "__main__":
    app.run(debug=True)
