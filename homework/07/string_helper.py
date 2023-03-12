def csv_to_list(csv):
    if type(csv) is not str:
        raise Exception("Give string object")

    csv_list = csv.split("\n")
    customers_list = []
    for item in csv_list:
        customer_data = item.split(",")
        customers_list.append(customer_data)
    
    return customers_list

def main():
    mj = "1,Jussi,Virtanen\n2,Pekka,Keinänen"
    print(csv_to_list(mj))

if __name__ == "__main__":
    main()
