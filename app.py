from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/test")
def hello_world():
    return "All is work"


@app.route('/')
def knopka():
    return render_template('base_page.html')


@app.route('/login', methods=['POST'])
def login():
    return 'Привет'


app.run(debug=True)
