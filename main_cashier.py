from modul_cashier import Transaction

def main():
    transaksi = Transaction()
    
    while True:
       
        print("Welcome to the self-service cashier system!")
        print("Select an option:")
        print("1. Add item")
        print("2. Update input item")
        print("3. Delete item")
        print("4. Reset transaction")
        print("5. Check orders")
        print("6. Calculate total purchase")
        print("7. Exit")
            
        choice = input("Select an option (1/2/3/4/5/6/7): ")
            
        if choice == '1':
            while True:
                try:
                    item_name = input("Item name: ")
                    item_qty = float(input("Item quantity (number only): "))
                    item_price = float(input("Item price (number only): "))
                    transaksi.add_item(item_name, item_qty, item_price)
                    print("The item has been added to the transaction.")
                    break  # stop the loop if the input is correct
                except ValueError:
                    print("Error: Item quantity and Item price must be numbers. Please try again.")
            transaksi.transaction_list()

        elif choice == '2':
            item_updated = False  # Initialize the item_updated variable
            while True:
                item_name = input("The name of the item you want to update: ")
                item_found = False  # Initialize the item_found variable

                for item in transaksi.items:
                    if item["item_name"] == item_name:
                        item_found = True
                        update_option = input("Select update option (name/quantity/price): ")

                        if update_option == "name":
                            new_name = input("New item name: ")
                            transaksi.update_item_name(item_name, new_name)
                            
                            print('Item name has been updated.')
                            break                                                                                                   
                            
                        elif update_option == "quantity" or update_option == "price":
                            while True:
                                try:
                                    new_value = float(input(f"New item {update_option}: "))
                                    if not isinstance(new_value, (int, float)):
                                        raise ValueError("New value must be a number")
                                    elif update_option == "quantity":
                                        transaksi.update_item_qty(item_name, new_value)
                                    else:
                                        transaksi.update_item_price(item_name, new_value)
                                                                        
                                    print(f"The {update_option} has been updated.")                                    
                                    break # stop the quantity and price loop if the input is correct

                                except ValueError:
                                    print(f"Error: New {update_option} must be a number.")
                                
                        else:
                            print("Invalid update option")                       
                        
                    elif not item_found:
                        print("The item that you want to change is not listed.")
                        break

                transaksi.transaction_list()
                update_completed = input("Update completed? (yes/no): ")
                if update_completed == "yes":                
                    break  # Stop the loop if the update is completed                            

        elif choice == '3':
            while True:
                item_name = input("Name of the item you want to delete: ")
                item_found = transaksi.delete_item(item_name)

                if item_found:     
                    print("The item has been removed from the transaction.")
                    break              
                elif not item_found:                 
                    print("The item that wants to be deleted is not listed")                

                    transaksi.transaction_list()
                delete_completed = input("Delete completed? (yes/no): ")
                if delete_completed.lower() == "yes":
                    break  # stoping loop if deleting is completed                             

        elif choice == '4':
            transaksi.reset_transaction()
            print("Transaction has been reset.")

        elif choice == '5':           
            result = transaksi.check_order()
            if result == "Everything is ok":
                print("Everything is ok.")
            else:
                print("Input error occurred in the transaction.")
            transaksi.transaction_list()

        elif choice == '6':
            total_price = transaksi.total_paid()
            print(f"Total to be paid: {total_price}")
            transaksi.transaction_list()

        elif choice == '7':
            print("Thank you for using our service.")
            break
        else:
            print("Invalid option. Please select the appropriate option (1/2/3/4/5/6/7).")          

if __name__ == "__main__":
    main()
