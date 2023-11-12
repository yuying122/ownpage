from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二B 411146287 施艾岑</h1>"
    homepage += "<a href=/me>自傳履歷</a><br>"
    homepage += "<a href=/hollandcode>興趣何倫碼測驗結果</a><br>"
    homepage += "<a href=/work>MIS相關工作</a><br>"
    homepage += "<a href=/webpage>查看連結</a><br>"
    return homepage


@app.route("/me")
def me():
    return render_template("me.html")

@app.route("/hollandcode")
def hollandcode():
    return render_template("hollandcode.html")  
    
@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/webpage")
def webpage():
    return render_template("webpage.html")          



if __name__ == "__main__":
    app.run()
