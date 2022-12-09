from flask import Flask, render_template, request
from main import main
import webbrowser, os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["inputbox"]
        out = main(text) if text != "" else ""

        print(f"> {text}")
        os.system(f'python speak.py "{out}"')
        text = ""

    return render_template("index.html")

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:8000/")
    app.run(port=8000)
