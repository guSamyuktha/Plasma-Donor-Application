from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
  return render_template('about.html')


@app.route("/aboutme")
def aboutme():
  return render_template('aboutme.html')

@app.route("/login")
def login():
  return render_template('login.html')

@app.route("/register")
def register():
  return render_template('register.html')