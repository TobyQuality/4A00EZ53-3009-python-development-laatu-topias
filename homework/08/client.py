import requests
from utils.user_input import *

def main():
    selected_choice = 1
    while selected_choice != -1:
        try:
            selected_choice = ask(["Add customer",
            "Delete customer with id", "Fetch all"])
        except Exception as e:
            print(e)
            selected_choice = None

        match selected_choice:
            case 1:
                given_name = input('Give name: ')
                name = {'name': given_name}

                url = 'http://127.0.0.1:5000/customers'
                x = requests.post(url, json = name)
                print(x.text)
            case 2:
                try:
                    id = ask_int("Give id: ", 0, 1000000)
                except Exception as e:
                    print(e)
                d = requests.delete(f"http://127.0.0.1:5000/customers/{id}")
                print(d.status_code)
            case 3:               
                r = requests.get('http://127.0.0.1:5000/customers')
                print(r.text)


if __name__ == "__main__":
    main()