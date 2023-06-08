"""Main script, uses other modules to generate sentences."""
from random_word import random_sentence
from histogram import histogram
from flask import Flask
import sys


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
histo = histogram(sys.argv)
sentence = random_sentence(histo)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    return f'<p>{sentence}</p>'


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
