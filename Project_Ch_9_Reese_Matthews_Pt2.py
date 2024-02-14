##Project: Product Inventory Management System


import pickle #the process of serializing an object is referred to as pickling 

with open('product_data.pkl', 'rb') as file:  ## load existing data from 'product_data.pkl' file using pickle
    products, categories, sales_transactions = pickle.load(file)

def display_products(products): #prints key and value in dict
    for key, value in products.items(): 
        print(f"{key}:")
        for inner_key, inner_value in value.items():
            print(f"    {inner_key}: {inner_value}")
        print()
        
##Implement functions to add, update, and delete products.
##let user add product
def add_product(product_inventory, categories):
    while True: 
        user_input = input("\nDo you want to add a new product? (y/n): ").lower() # asks users confirmation to proceed
        if user_input == "n":
            print("\nNo new products have been added.\n") # if user chooses not to add a product, displays current products/categories and exits function
            display_products(product_inventory)
            #print(products)
            #print(categories)
            return
        elif user_input == "y": # user chooses to add a product
            break
        else:
            print("Invalid: Please enter 'y' for yes or 'n' for no.")
        
    while True: 
        try: 
            product_id = int(input("\nEnter Product ID: "))  # gets product details from user and validate inputs with error handling
            if product_id in products:
                print("ERROR! Product ID already exists. Please try again.")
                continue
            product_name = input("Enter Product Name: ") # gathers product info from the users input
            product_price = float(input("Enter Product Price: "))
            product_quantity = int(input("Enter Product Quantity: "))
            product_category = input("Enter Product Category: ")

            products[product_id] = { # updates products in dictionary
                'name': product_name,
                'price': product_price,
                'quantity': product_quantity,
                'category': product_category
            }
            
            categories.add(product_category)#if the user adds a new category

            print("\nProduct has been added successfully.")
            display_products(product_inventory)
            break  # exits the loop after adding product 

        except ValueError:
            print("Error: Invalid input.") # handles invalid entry

##let user update an existing product
def update_product(product_inventory, categories):
    while True: # loops to handle user input for updating an existing product
        user_input = input("\nDo you want to update a product? (y/n): ").lower() #asks user if they want to udpate a product 
        if user_input == "n":   #if the user chooses not to update an existing product, it displays current products and categories
            print("\nNo products have been updated.\n")
            display_products(product_inventory)
            #print(products)
            #print(categories)            
            return
        elif user_input == "y": #if user chooses to update a product
            break
        else:
            print("Invalid: Please enter 'y' for yes or 'n' for no.") #tells the user to enter an invaild response 
    while True:
        try:
            product_id = int(input("\nEnter the Product ID you want to update: ")) #asks the user which ID they want to update
            if product_id not in products:
                print("Error: Product ID does not exist. Please try again.") #product not in inventory 
                return

            print(f"Current details: {products[product_id]}") # displays current details of the selected product
            product_name = input("Enter new product name or press Enter to keep unchanged: ") #tells the user to enter new name or leave it blank to keep it unchanged 
            if product_name:
                products[product_id]['name'] = product_name

            try:
                product_price = input("Enter new product price or press Enter to keep unchanged: ") #tells the user to enter new price or leave it blank to keep it unchanged 
                if product_price:
                    products[product_id]['price'] = float(product_price)

                product_quantity = input("Enter new product quantity or press Enter to keep unchanged: ") #tells the user to enter new quantity or leave it blank to keep it unchanged 
                if product_quantity:
                    products[product_id]['quantity'] = int(product_quantity)

                product_category = input("Enter new product category or press Enter to keep unchanged: ") #tells the user to enter new category or leave it blank to keep it unchanged 
                if product_category:
                    products[product_id]['category'] = product_category
                    categories.add(product_category)

                print("\nProduct has been updated successfully.\n") #lets the user know that the product was successfully done
                display_products(product_inventory)
                #print(products)
                #print(categories)
                break

            except ValueError:
                print("Error: Please enter a valid entry.") #error handling for price or quantity 

        except ValueError:
            print("Error: Please enter a valid Product ID.") #error handling for product id 

##lets user delete products
def delete_product():
    while True:
        user_input = input("\nDo you want to delete a product? (y/n): ").lower() #asks user if they want to delete a product 
        if user_input == "n":
            print("\nNo products have been deleted.\n") #lets the user know that no products have been deleted 
            return
        elif user_input == "y": #if the user enters y then it gives the user access to enter product details 
            try:
                product_id = int(input("\nEnter the Product ID you want to delete: "))
                if product_id in products: #if the id is in products then it gets deleted 
                    del products[product_id] # deletes the product from inventory and confirms
                    print(f"Product with ID {product_id} has been deleted successfully.")
                    display_products(products)                    
                    return
                else:
                    print("Error: Product ID does not exist. Please try again.") #tells the user that ID does not exist and to try again 
            except ValueError:
                print("Invalid: Please enter a valid Product ID.") #tells the user to enter valid ID 
        else:
            print("Invalid: Please enter 'y' for yes or 'n' for no.") #tells the user to enter y or n

#record sales transactions in a dictionary (product ID, quantity sold) 
def record_sale(): 
    try:
        product_id = int(input("Enter the Product ID for the sale: ")) #asks the user to enter ID for the sale 
        if product_id not in products: #if the ID is not in products then ID does not exist 
            print("Error: Product ID does not exist.") #gives user an error
            return
        quantity_sold = int(input("Enter the quantity sold: ")) #asks the user how sold 
        if quantity_sold > products[product_id]['quantity']: #if quantity sold is more than then products available then it gives the user an error 
            print("Error: Insufficient quantity in stock.") #tells user out of stock 
            return
        products[product_id]['quantity'] -= quantity_sold #subtacts sold from available quantity. reduces the quantity of the product in stock by the amount sold.
        sales_transactions[product_id] = sales_transactions.get(product_id, 0) + quantity_sold #records the sales transaction. adds the quantity sold in the current transaction to the total sales for this product.
        print("Sale has been recorded successfully.")

    except ValueError:
        print("Invalid: Please enter valid values.") #error to user

#Use dictionary comprehensions to summarize sales data
def summarize_sales():
    print("\nSales Summary:") #tells user sales summary
    total_revenue = 0  #initialized to 0

    for product_id, quantity in sales_transactions.items():
        if product_id in products: #checks current id exists in products 
            product_name = products[product_id]['name'] #gets name 
            category = products[product_id]['category']  #gets category 
            sales_amount = products[product_id]['price'] * quantity #calculates the total sales amount for the product
            total_revenue += sales_amount #running total of revenue
            print(f"Product ID: {product_id}, Name: {product_name}, Category: {category}, Quantity Sold: {quantity}, Sales Amount: ${sales_amount:.2f}")
        else:
            print(f"Product ID: {product_id} not found in inventory.") #tells user id was not found 

    print(f"Total Revenue from Sales: ${total_revenue:.2f}") #shows user sales revenue
    
##Generate reports on inventory levels, sales performance, and product categories.

#report on inventory 
def inventory_report(product_inventory):
    print("\nInventory Levels Report:")
    for product_id, details in product_inventory.items(): #shows products in inventory 
        print(f"Product ID: {product_id}, Name: {details['name']}, Quantity: {details['quantity']}, Category: {details['category']}") #prints each product 
#report on sales performance 
def sales_performance_report(sales_transactions, product_inventory):
    if not sales_transactions: #if no sales have been made 
        print("\nSales Performance Report:\nNo sales have been recorded.\n")
        return
    category_sales = {} #stores sales data by categories 
    favorite_product = {'id': None, 'sales': 0} #highest id sales and sales amount 

    for product_id, quantity in sales_transactions.items():
        if product_id in product_inventory: #if id in product inventory 
            category = product_inventory[product_id]['category']
            sales_amount = product_inventory[product_id]['price'] * quantity #calculates the total sales amount for this product by multiplying the products price by the quantity sold
            
            category_sales[category] = category_sales.get(category, 0) + sales_amount #accumulates sales amounts

            if sales_amount > favorite_product['sales']: #determines the product with the highest sales amount 
                favorite_product = {'id': product_id, 'sales': sales_amount}

    print("\nSales Performance Report")
    print("\nSales by Category:")
    for category, sales in category_sales.items(): #contains sales data categorized by product category
        print(f"Category: {category}, Total Sales: ${sales:.2f}") #prints category and total sales

    if favorite_product['id'] is not None: #no product has been identified as the favorite 
        fav_product_details = product_inventory[favorite_product['id']] #if a favorite product exists
        print(f"\nFavorite Product of the Day: {fav_product_details['name']} (ID: {favorite_product['id']}), Total Sales: ${favorite_product['sales']:.2f}") #displays name of the favorite product, ID, and total sales amount
    else:
        print("\nFavorite Product of the Day: None") #no product has been identified

#Use set operations to analyze product categories           
def category_analysis(product_inventory):
    print("\nProduct Categories Analysis:")
    all_categories = set() # empty set, it will be used to store each unique category found in the inventory
    for details in product_inventory.values():
        all_categories.add(details['category']) #collects all unique categories 
    
    print(f"All Categories: {all_categories}") #prints categories 

#Implement pickling to serialize and save dictionaries to a file
def save_data():
    with open('product_data.pkl', 'wb') as file: #write-binary mode
        pickle.dump((products, categories, sales_transactions), file) #method to serialize the products, categories, and sales transactions
    print("Data has been saved successfully.") #tells the user that the data has been saved

#Load and unpickle dictionaries from a file to retrieve stored data
def load_data(): #used to load previously saved inventory data from a file
    global products, categories, sales_transactions
    try:
        with open('product_data.pkl', 'rb') as file: #read-binary mode 
            products, categories, sales_transactions = pickle.load(file) #deserialize and load the data from the file
        print("Data has been loaded successfully.")#tells the user that the data has been loaded
    except FileNotFoundError: #occurs if pkl doesnt exist 
        print("No saved data has been found.")
        products = {} #empty dictionary
        categories = set()
        sales_transactions = {}       

# Main function
def main(): #gives the user options to choice from the menu 
    while True:
        print("\nEXOTIC PETS AND DOGS PRODUCT INVENTORY MANAGEMENT SYSTEM:\n")
        print("1. Add a new product to inventory")
        print("2. Update an existing product ")
        print("3. Delete a product from inventory")
        print("4. Record a sale")
        print("5. Show sales summary")
        print("6. Inventory Levels Report")
        print("7. Sales Performance Report")
        print("8. Product Categories Analysis")
        print("9. Save Data")
        print("10. Exit\n")
        

        selection = input("Enter your choice (1-10): ") #gives the user the option 1 - 10 

        if selection == '1':
            add_product(products, categories)
        elif selection == '2':
            update_product(products, categories)
        elif selection == '3':
            delete_product()
        elif selection == '4':
            record_sale()
        elif selection == '5':
            summarize_sales()
        elif selection == '6':
            inventory_report(products)
        elif selection == '7':
            sales_performance_report(sales_transactions, products)
        elif selection == '8':
            category_analysis(products)
        elif selection == '9':
            save_data()
        elif selection == '10':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please enter a number between 1-10")

if __name__ == "__main__":
    main()
