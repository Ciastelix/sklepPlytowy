from app import app
from flask import url_for, redirect, render_template, Blueprint, request, flash

muzyka = Blueprint(
    "muzyka", __name__, static_folder="static", template_folder="templates"
)


@muzyka.route("/")
def wszystko():
    return render_template("muzyka.html")

@muzyka.route("/winyle")
def winyle():
    return render_template("winyle.html")
@muzyka.route("/cd")
def cd():
    return render_template("cd.html")