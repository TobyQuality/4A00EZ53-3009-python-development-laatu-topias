from flask import Flask
from flask import render_template
from flask import request
from repository import *
from string_helper import *
from validation import *

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name'] # get user input from post
        return render_template('index.html', name=name)
    return render_template('index.html', name="Jack")

@app.route('/name-form', methods = ['POST', 'GET'])
def name_form():
    if request.method == 'POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        name = f"{fname} {lname}"
        if is_name(name):
            save_to_database(fname, lname)
            return render_template('name-form.html', notification=f'{name} added to database')
        else:
            return render_template('name-form.html', notification=f'Name did not pass validation check')
    return render_template('name-form.html')

@app.route('/database', methods = ['POST', 'GET'])
def database():
    db_str = read_database()
    db_list = csv_to_list(db_str)
    if request.method == 'POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        name = f"{fname} {lname}"
        if is_name(name):
            save_to_database(fname, lname)
            db_str = read_database()
            db_list = csv_to_list(db_str)
            return render_template("database.html", customers=db_list)
        else:
            return render_template("database.html", customers=db_list, notification="Adding customer to database failed")

    return render_template("database.html", customers=db_list)

if __name__ == "__main__":
    app.run(debug=True)