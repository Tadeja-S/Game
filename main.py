from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)

@app.route("/")
def index():
    secret_number = request.cookies.get("secret_number")
    
    response = make_response(render_template("index.html"))
    if not secret_number:
        new_secret = random.randint(1, 20)
        response.set_cookie("secret_number", str(new_secret))
    
    return response

@app.route("/answer", methods=["POST"])
def answer():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        message = "Congratulations! You guessed the secret number."
        response = make_response(render_template("answer.html", message=message))
        new_secret = random.randint(1, 20)
        response.set_cookie("secret_number", str(new_secret))
        return response

    elif guess > secret_number:
        message = "Nope. Try something smaller."
        return render_template("answer.html", message=message)
    
    elif guess > secret_number:
        message = "Nope. Try something bigger."
        return render_template("answer.html", message=message)

if __name__ == '__main__':
    app.run(use_reloader=True)