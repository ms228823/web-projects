import os
from datetime import date
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///technica.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def newsletter():
    """Log user in"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not (newsletter := request.form.get("newsletter")):
            warning = 1
            return render_template(
                "login.html",
                warning=warning,
            )
        # Query database for username
        newsletter_subscribers = db.execute(
            "SELECT * FROM newsletter_subscribers ;"
        )

        # Ensure username exists and password is correct
        if newsletter != 1 not in newsletter_subscribers[1]["email"] ( 
            newsletter_subscribers[0]["hash"], request.form.get("password")
        ):
            warning = 2
            return render_template(
                "login.html",
                warning=warning,
            )
        db.execute("INSERT INTO newsletter_subscribers VALUES(?);",newsletter)
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html")
