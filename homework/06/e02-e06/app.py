from flask import Flask
import datetime

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)

# if url is in root
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/myname")
def my_name():
    return "<p>Topias</p>"

@app.route("/date")
def date():
    date = datetime.datetime.now()
    return date.strftime("%Y-%m-%d %H:%M:%S.%f")

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)