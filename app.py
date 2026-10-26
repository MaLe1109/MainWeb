
from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.route("/anfrage", methods=["POST"])
def anfrage():
    name = request.form.get("name")
    beschreibung = request.form.get("beschreibung")

    print("Neue Anfrage:", name, beschreibung)

    return redirect(url_for("baymeth"))


@app.route("/abo", methods=["POST"])
def abo():
    name = request.form.get("name")
    email = request.form.get("email")

    print("Neue Buchung:", name, email)

    return redirect(url_for("baymeth"))


@app.route("/baymeth")
def baymeth():
    return app.send_static_file("baymeth.html")


if __name__ == "__main__":
    app.run(debug=True)
