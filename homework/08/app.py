from flask import *
from json import *
import random
from repository import *

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route("/")
def root():
    return "<h1>hello</h1>"

@app.route("/customers")
def get_customers():
    customers = fetch_customers()
    my_response = jsonify(customers)
    return make_response(my_response, 200)

@app.route('/customers/<int:the_id>')
def get_customer(the_id):
    customers = fetch_customers()
    searchedCustomer = None
    for customer in customers:
        if customer['id'] == the_id:
            searchedCustomer = jsonify(customer)
            break
    if searchedCustomer != None:
        return make_response(searchedCustomer, 200)
    else:
        abort(404)

@app.route('/customers/<int:the_id>', methods=['DELETE'])
def delete_customer(the_id):
    customers = fetch_customers()
    index = -1
    for i in range(0, len(customers)):
        if customers[i]['id'] == the_id:
            index = i
            break
    if index != -1:
        customers.pop(index)
        try:
            overwrite_database(customers)
        except Exception as e:
            print(e)
            abort(500)
        return make_response("", 204)
    else:
        abort(404)

@app.route('/customers', methods=['POST'])
def add_customer():
    customers = fetch_customers()
    # only name attribute from request's data will be picked up
    customer = json.loads(request.data)
    customer_name = customer['name']
    generated_id = int(1000000 * random.random())
    for i in range(0, len(customers)):
        if customers[i]['id'] == generated_id:
            return make_response(jsonify("Error: id already exists"), 409)
    save_to_database(customer_name, str(generated_id))
    return make_response("", 201)

if __name__ == "__main__":
    app.run(debug = True)