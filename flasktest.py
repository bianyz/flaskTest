from flask import *

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template("index.html")
    #return redirect(url_for("login"))


@app.route('/login')
def login():
    return render_template("login.html")
    #return redirect("login.html")
