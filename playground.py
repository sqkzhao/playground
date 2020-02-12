from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def play():
    return render_template("index.html", x = 3, color = "blue")

@app.route("/play/<int:x>")
def play_x(x):
    return render_template("index.html", x = int(x), color = "blue")

@app.route("/play/<int:x>/<color>")
def play_x_color(x, color):
    return render_template("index.html", x = int(x), color = color)

if __name__ == "__main__":
    app.run(debug=True)