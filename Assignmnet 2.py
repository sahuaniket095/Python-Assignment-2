# Product Class
class Product:
    def __init__(self, name, price, quantity, product_type):    
        # Initializing a product class which contains name, price, quantity, and type.
        self.name = name
        self.price = price
        self.quantity = quantity
        self.product_type = product_type

    def __str__(self):
        # Returning a string representation of the product.
        return f"Product Name: {self.name}, Price: {self.price} RS, Quantity: {self.quantity}, Type: {self.product_type}"

    def update_quantity(self, quantity_sold):
        # Updating the quantity after a sale.
        self.quantity -= quantity_sold

    def restock(self, quantity_added):
        # Restocking a product.
        self.quantity += quantity_added

    def calculate_price(self, quantity_bought):
        # Calculating the total price for the quantity purchased.
        return round(self.price * quantity_bought, 2)

# Inventory Class
class Inventory:
    def __init__(self):
        # Initializing the inventory with an empty list of products.
        self.products = []

    def add_product(self, product):
        # Adding a new product to the inventory.
        self.products.append(product)

    def remove_product(self, product_name):
        # Removing a product by name from the inventory.
        self.products = [product for product in self.products if product.name.lower() != product_name.lower()]

    def list_all_products(self):
        # Listing all products in the inventory.
        if not self.products:
            return "Please add products first. Inventory is empty."
        return "\n".join(str(product) for product in self.products)

    def count_products(self):
        # Returning the total number of products in the inventory.
        return len(self.products)

    def list_products_by_type(self, product_type):
        # Listing products by a specific type.
        filtered_products = [product for product in self.products if product.product_type.lower() == product_type.lower()]
        if not filtered_products:
            return f"No products found under the type '{product_type}'."
        return "\n".join(str(product) for product in filtered_products)

    def find_product_by_name(self, product_name):
        # Finding a product by name.
        for product in self.products:
            if product.name.lower() == product_name.lower():
                return product
        return None


def input_with_error_handling(prompt, value_type=float):
    # Helper function which safely handles user inputs.
    while True:
        try:
            value = value_type(input(prompt))  # Attempt to convert the input to the desired type
            return value
        except ValueError:  # If conversion fails, ValueError is raised
            print(f"Invalid input. Please enter a valid {value_type.__name__} value.")  # Show an error message

# Defining main function
def main():
    # Main function for interaction of user with inventory system.
    inventory = Inventory()

     # Displays a menu of options for the user to interact with the inventory system.
    while True:
        print("\nOptions:")
        print("1. View All Products")
        print("2. Add a New Product")
        print("3. View Products by Type")
        print("4. Remove Product by Name")
        print("5. Add Stock to Product")
        print("6. Purchase Products")
        print("7. Exit")

        # Takes user input for selecting an option.
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            # Option to display all products in the inventory.
            print("\nAll Products in Inventory:")
            print(inventory.list_all_products())
            print("\nTotal number of products:", inventory.count_products())

        elif choice == '2':
            # Option to add a new product to the inventory.
            print("\n--- Add a New Product ---")
            name = input("Enter  the product name: ")

            # Using the input_with_error_handling function for price and quantity to ensure correct values are entered
            price = input_with_error_handling("Enter product price (in Rs.): ", float)
            quantity = input_with_error_handling("Enter product quantity: ", int)  # Added error handling for quantity input
            product_type = input("Enter product type: ")

            new_product = Product(name, price, quantity, product_type)
            inventory.add_product(new_product)
            print(f"\nNew product {name} added to inventory.")

        elif choice == '3':
            # Option to view products by a specific type.
            print("\n--- View Products by Type ---")
            product_type = input("Enter product type (e.g., Leafy green, Root, etc.): ")
            print(f"\nProducts of type '{product_type}':")
            print(inventory.list_products_by_type(product_type))

        elif choice == '4':
            # Option to remove a product from the inventory by name.
            print("\n--- Remove a Product ---")
            product_name = input("Enter the name of the product  you want to remove: ")
            product = inventory.find_product_by_name(product_name)
            if product:
                inventory.remove_product(product_name)
                print(f"\n{product_name} has been removed from the inventory.")
            else:
                print(f"\n{product_name} not found in inventory.Please add the product into Inventory First")

        elif choice == '5':
            # Option to restock an existing product in the inventory.
            print("\n--- Restock Product ---")
            product_name = input("Enter the product name to restock: ")
            quantity_to_add = input_with_error_handling("Enter the quantity to add: ", int)
            product = inventory.find_product_by_name(product_name)
            if product:
                product.restock(quantity_to_add)
                print(f"\nRestocked {quantity_to_add} of {product_name}.")
            else:
                print(f"\n{product_name} not found in inventory. Please add the Product in inventory First")

        elif choice == '6':
            # Option to purchase products from the inventory.
            print("\n--- Purchase Products ---")
            total_cost = 0
            product_purchased = False
            while True:
                product_name = input("Enter the product you want to purchase (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break
                product = inventory.find_product_by_name(product_name)
                if product:
                    quantity = input_with_error_handling(f"Enter quantity of {product_name}: ", int)
                    if quantity <= product.quantity:
                        total_cost += product.calculate_price(quantity)
                        product.update_quantity(quantity)
                        print(f"{quantity} of {product_name} purchased.")
                        product_purchased = True
                    else:
                        print(f"Not enough stock for {product_name}. Only {product.quantity} available.")
                else:
                    print(f"{product_name} not found in inventory.")

             # If any product was purchased, show the total cost; otherwise, display a message.
            if product_purchased:
                print(f"\nTotal cost for your purchase: {total_cost} RS")
            else:
                print("No products purchased.")
       
        # Option to exit the inventory management system.
        elif choice == '7':
            print("\nExiting Inventory Management System.")
            break
        
        # If the user enters an invalid option, display an error message.
        else:
            print("\n Please try again. Your choice is invalid.")

# Start the program by calling the main function.
if __name__ == "__main__":
    main()
