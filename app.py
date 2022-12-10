from flask import Flask, render_template, request
import webbrowser, os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["inputbox"]

        if text:
            with open("assets\\current.txt", "w") as f: f.write(text)

        text = ""

    return render_template("index.html")

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:8000/")
    os.system("start python main.py")
    app.run(port=8000)
