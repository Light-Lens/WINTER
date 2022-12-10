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
        with open("assets\\current.txt", "w") as f: f.write("")

    return render_template("index.html")

if __name__ == "__main__":
    os.system("start python main.py")
    webbrowser.open("http://127.0.0.1:8000/")
    app.run(port=8000)
