from flask import Flask, render_template, url_for
import glob

app = Flask(__name__)

@app.route("/")
def index():
    imagesSrc = glob.glob("static/pictures/*")
    return render_template("index.html", imagesSrc = imagesSrc)

if __name__ == "__main__":
    app.run(debug=True)