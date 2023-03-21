def read_database():
    data = open("database.txt", "r")
    return data.read()

def save_to_database(name, id):
    f = open("database.txt", "a")
    f.write(f"\n{id},{name}")
    f.close()

#used with delete
def overwrite_database(db_list):
    f = open("database.txt", "w")
    for i in range(len(db_list)):
        id = db_list[i]['id']
        name = db_list[i]['name']
        if len(db_list) - 1 > i:
            f.writelines(str(id) + ',' + name + '\n')
        else:
            #last line of database.txt must not be empty,
            #pr it will break the code
            f.writelines(str(id) + ',' + name)
    f.close()

def fetch_customers():
    customers = []
    database_content = read_database()
    db_split = database_content.split('\n')
    for data in db_split:
        attributes = data.split(',')
        customer = {'id': int(attributes[0]), 'name': attributes[1]}
        customers.append(customer)
    return customers

def main():
    print(read_database())

if __name__ == "__main__":
    main()