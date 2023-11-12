from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二B 411146287 施艾岑</h1>"
    homepage += "<a href=/homepage>個人網站</a><br>"
    return homepage


@app.route("/homepage")
def homepage():
    return render_template("homepage.html")



if __name__ == "__main__":
    app.run()
