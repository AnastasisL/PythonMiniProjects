def output_all():
    #Output all the products in the file
    print("------------------------------------")
    text_file = open("Objective 10 - Product catalogue.txt", "r")
    while True:
        product_description = text_file.readline().strip()
        product_price = text_file.readline().strip()
        if not product_description: break
        print(product_description)
        print(product_price)
    text_file.close()
    print("------------------------------------")

def output_product(product_to_find):
    #Use a linear search to find a product
    print("------------------------------------")
    search_complete = False
    text_file = open("Objective 10 - Product catalogue.txt", "r")
    while not search_complete:
        #Read in a product from the file
        product_description = text_file.readline().strip()
        product_price = text_file.readline().strip()
        #Handle the end of the file being reached
        if not product_description:
            print("Product not found.")
            search_complete = True
        #Product found
        if product_description == product_to_find:
            print(product_description)
            print(product_price)
            search_complete = True
    text_file.close()
    print("------------------------------------")

def add_product(product_description,product_price):
    #Add a product to the catalogue
    text_file = open("Objective 10 - Product catalogue.txt", "a")
    text_file.write(product_description+"\n")
    text_file.write(product_price+"\n")
    text_file.close()
    print("Product added")

def menu():
    #User interface
    choice = ""
    while choice != "4":
        print("1. Output all products")
        print("2. Find a product")
        print("3. Add a product")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            output_all()
        if choice == "2":
            product_to_find = input("Enter the product to find: ")
            output_product(product_to_find)
        if choice == "3":
            product_description = input("Enter the product description: ")
            product_price = input("Enter the price: ")
            add_product(product_description,product_price)
