from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "immasecret"
toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()
scores = []

board = boggle_game.make_board()
size = len(board)

@app.route("/")
def homepage():
    """Show board."""
    session['board'] = board

    return render_template("board.html", board=board)


@app.route("/check-word")
def check_word():
    """Check if word is in dictionary."""

    word = request.args["word"]
    word = word.lower() #make word lowercase
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/scores")
def score_board():
    """Show list of scores"""
    session['scores'] = 
    return render_template("scores.html", scores=scores)


