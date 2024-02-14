##Project: Product Inventory Management System

import pickle #the process of serializing an object is referred to as pickling 

def main():
##Create and manipulate a dictionary to store product details (ID, name, price, quantity).
    products = {
        1: {'name': 'Boston Terrier', 'price': 1000.00, 'quantity': 10, 'category': 'Dogs'}, 
        2: {'name': 'Shiba Inu', 'price': 2000.00, 'quantity': 8, 'category': 'Dogs'},
        3: {'name': 'Raccoon', 'price': 3000.00, 'quantity': 5, 'category': 'Exotic Pets'},  
        4: {'name': 'Skunk', 'price': 4000.00, 'quantity': 2, 'category': 'Exotic Pets'},
        5: {'name': 'Shark Ball', 'price': 5000.00, 'quantity': 6, 'category': 'Toys'},
        6: {'name': 'Moo Moo', 'price': 1500.00, 'quantity': 2, 'category': 'Toys'},
            }
## set operations to categorize products (e.g., electronics, groceries).
    categories = {'Dogs', 'Exotic Pets', 'Toys'} 
    sales_transactions = {} #used to store information about sales transactions

    objects_to_pickle = [products, categories, sales_transactions] # Bundle the objects into a list to prepared for serialization

    with open('product_data.pkl', 'wb') as file: #write-binary mode 
        pickle.dump(objects_to_pickle, file) #pickle 
    
    with open('product_data.pkl', 'rb') as file: #read-binary mode
        products, categories, sales_transactions = pickle.load(file)

    for key, value in products.items(): # Loop through each item in the dictionary and print
        print(f"{key}:")
        for inner_key, inner_value in value.items():
            print(f"    {inner_key}: {inner_value}")
        print() #this line just prints a blank line for spacing

if __name__ == "__main__":
    main()
