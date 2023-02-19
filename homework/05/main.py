import util.user_input
import util.string_helper

def main():
    employees = []
    input = 1
    while input != -1:
        print("Employees\n", employees)
        input = util.user_input.ask(["Add"])
        if input == 1:
            employee = util.user_input.ask_person()
            employees.append(employee)
        if input == -1:
            return

main()