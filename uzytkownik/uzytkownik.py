from app import app
from flask import url_for, redirect, render_template, Blueprint, request, flash

uzytkownik = Blueprint(
    "uzytkownik", __name__, static_folder="static", template_folder="templates"
)


@uzytkownik.route("/")
def stronaUzytkownika():
    return render_template("strona_uzytkownika.html")


@uzytkownik.route("/rejstracja/", methods=["POST", "GET"])
def rejstracja():
    if request.method == "POST":
        flash(["Udało się", "Zarejestrowano pomyślnie, możesz sie zalogować"])
        return redirect(url_for("login"))
    else:
        return render_template("rejstracja.html")


@uzytkownik.route("/zaloguj/", methods=["POST", "GET"])
def zaloguj():
    if request.method == "POST":
        return redirect(url_for("stronaUzytkownika"))
    else:
        return render_template("login.html")


@uzytkownik.route("/wyloguj/")
def wyloguj():
    return "Hey"
