from flask import Flask
from flask import request
from htmlhelper import *
import datetime
import random

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
    date = date.strftime("%Y-%m-%d %H:%M:%S.%f")
    date_in_paragraph = f"<p>{date}</p>"
    html_page = generate_html_page("date", date_in_paragraph)
    return html_page

@app.route("/slot-machine")
def slot_machine():
    content="<div>\n"
    slots = ["cherries.jpg", "gold-coin.png", "seven.png"]
    chosen_slots = []
    for i in slots:
        slot = random.choice(slots)
        chosen_slots.append(slot)
        # using tabulators to make the html code more readable
        content = content + f"      <img src=\"static/{slot}\">\n"

    content = content + "    </div>"
    win = True
    for i in range(0, len(chosen_slots) - 1):
        if chosen_slots[i] != chosen_slots[i+1]:
            win = False
            break
    if win:
        content = content + f"\n    <h1>Win!</h1>"
    
    html_page = generate_html_page("slot-machine", content)
    return html_page

@app.route("/bmi")
def bmi_calculator():
    if request.args.get('mass') == None or request.args.get('height') == None:
        return generate_bmi_form()
    mass = int(request.args.get('mass'))
    height = float(request.args.get('height'))
    if mass <= 0 or height <= 0 or mass > 500 or height > 3.00:
        return generate_bmi_form("<h1>Fail!</h1>")
    else:
        bmi = mass / (height * height)
        bmi = round(bmi, 1)
        result = f"<h3>{bmi}</h3>"
        return  generate_bmi_form(result)

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)