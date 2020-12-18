# from boggle import Boggle
# from flask import Flask, request, render_template, redirect, session, jsonify
# from flask_debugtoolbar import DebugToolbarExtension

# boggle_game = Boggle()


# app = Flask(__name__)
# app.config['SECRET_KEY'] = "abc123"
# app.debug = True
# toolbar = DebugToolbarExtension(app)

# gameboard = Boggle.make_board(boggle_game)
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# highscore = 0

# @app.route('/', methods=["POST", "GET"])
# def home_page():
#     session['board'] = gameboard
#     size = range(len(gameboard))
#     return render_template('board.html', gameboard=gameboard, size=size, highscore=highscore)

# @app.route('/check_word', methods=["POST"])
# def check_word():
#     word = request.form["word"]
#     board = session["board"]
#     response = boggle_game.check_valid_word(board, word)

#     return jsonify({'result': response})

# @app.route("/post-score", methods=["POST"])
# def post_score():
#     score = request.json["score"]
#     highscore = session.get("highscore", 0)
#     session['highscore'] = max(score, highscore)

#     return jsonify(brokeRecord=score > highscore)

from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "immasecret"
app.debug = True
toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

board = boggle_game.make_board()
size = len(board)

@app.route("/")
def homepage():
    """Show board."""
    session['board'] = board

    return render_template("board.html", board=board)



@app.route("/check-word", methods=["POST"])
def check_word():
    """Check if word is in dictionary."""

    word = request.form["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

