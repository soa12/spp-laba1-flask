import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request
app = Flask(__name__)
logging.basicConfig(filename='example.log',level=logging.INFO)

@app.route("/")
def index():
     return render_template('index.html', status = 'App runnig')
app.add_url_rule('/', 'index', index)

@app.route("/action")
def action():
    template_variable = request.args.get('submit')
    return render_template('index.html', status=template_variable)

@app.route("/show-logs")
def get_logs():
    logs = open('example.log')
    template_variable = [log for log in logs]
    return render_template('logs.html', logs=template_variable)

if __name__ == "__main__":
    app.debug = True
    app.run()