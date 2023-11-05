from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, item_qty, item_price):
        """
        Add item to transaction.

        Args:
            item_name (str): Item Name.
            item_qty (int): Item Quantity.
            item_price (int): Item Price.

        """
        self.items.append({"item_name": item_name, "item_qty": item_qty, "item_price": item_price})

    def update_item_name(self, old_name, new_name):
        """
        Updating Item Name.

        Args:
            old_name (str): Item name that want to be updated.
            new_name (str): New item name.

        """
        for item in self.items:
            if item["item_name"] == old_name:
                item["item_name"] = new_name

    def update_item_qty(self, item_name, new_qty):
        """
        Updating Item Quantity.

        Args:
            item_name (str): Item name that the quantity want to be updated.
            new_qty (int): New item quantity.

        """
        for item in self.items:
            if item["item_name"] == item_name:
                item["item_qty"] = new_qty

    def update_item_price(self, item_name, new_price):
        """
        Updating Item price.

        Args:
            item_name (str): Item name that the price want to be updated.
            new_price (int): New item price.

        """
        for item in self.items:
            if item["item_name"] == item_name:
                item["item_price"] = new_price

    def delete_item(self, item_name):
        """
        Delete an item from the transaction.

        Args:
            item_name (str): The name of the item to be deleted.

        Returns:
            bool: True if the item is found and deleted, False if the item is not found.
        """
        initial_item_count = len(self.items)
        self.items = [item for item in self.items if item["item_name"] != item_name]
        return len(self.items) < initial_item_count


    def reset_transaction(self):
        """
        Deleting all. Reset all the transaction.

        """
        self.items = []

    def check_order(self):
        """
        Check the transaction for input errors.

        Returns:
            str: The message "Everything is ok" if there are no input errors, or "There is an input error" if there is an input error.

        """
        for item in self.items:
            if not (item["item_name"] and item["item_qty"] and item["item_price"]):
                return "There's an input error."
        return "Everything is ok"


    def total_paid(self):
        """
        Calculate the total shopping price.

        Returns:
            int: Total shopping price after discount.

        """
        total = sum(item["item_qty"] * item["item_price"] for item in self.items)

        if total > 500000:
            discount = 0.10  # 10% discount
        elif total > 300000:
            discount = 0.08  # 8% discount
        elif total > 200000:
            discount = 0.05  # 5% discount

        if discount is not None:
            total *= (1 - discount)
            print(f'You get {float(discount * 100)}% discount.')

        return total

    def transaction_list(self):
        """
        Show the transaction list on the screen.

        """
        data = []
        total = 0
        for i, item in enumerate(self.items, 1):
            item_name = item["item_name"]
            item_qty = item["item_qty"]
            item_price = item["item_price"]
            total_item_price = item_qty * item_price
            total += total_item_price
            data.append([i, item_name, item_qty, item_price, total_item_price])

        # Add total spending to data
        data.append(["Overall total", "", "", "", total])

        # Use tabulate to print tables
        headers = ["No", "Item Name", "Item Quantity", "Item Price", "Total Price"]
        print(tabulate(data, headers, tablefmt="grid"))