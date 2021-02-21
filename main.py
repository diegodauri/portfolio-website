from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib

app = Flask(__name__)

app.config["SECRET_KEY"] = "fenjseKN3734£82"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form", methods=["POST"])
def form():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="dauridiego.test@gmail.com", password="Pa$$word1234")
        connection.sendmail(from_addr="dauridiego.test@gmail.com", to_addrs="dauridiego@gmail.com",
                            msg=f"Subject:New Message\n\n\nname: {name}\nemail: {email}\nmessage: {message}")

    flash("message sent")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
