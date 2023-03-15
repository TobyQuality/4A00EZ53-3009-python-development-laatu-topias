import util.user_input
import util.string_helper

def main():
    employees = []
    input = 1
    while input != -1:
        print("Employees\n", employees)
        try:
            input = util.user_input.ask(["Add"])
        except Exception as e:
            print(e)
            input = ""
        if input:
            if input == 1:
                employee = util.user_input.ask_person()
                employees.append(employee)
            if input == -1:
                return
main()