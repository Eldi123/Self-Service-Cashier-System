# Self-Service Cashier System

This project is a personal Python coding exercise designed to create a self-service cashier system. The primary goal is to help Andi, the owner of a large supermarket in Indonesia, automate the checkout process for his customers. With this system, customers can conveniently enter the items they purchase, specify quantities, prices, and access additional features, even if they are not physically present at the supermarket.

## Table of Contents
1. [Background](#background)
2. [Usage](#usage)
3. [Features](#features)
4. [Development](#development)

## Background
Andi, a large supermarket owner in Indonesia, plans to use a self-service cashier system in his supermarket so that customers can directly enter the items purchased, the quantity purchased, and the price of the items purchased, and other features. So that customers who are not in the city can buy goods from the supermarket.

## Usage
This program is basically a CLI-based program which is still in the development stage and to use it in a more commercial scope it is necessary to improvise the code for a GUI-based program. This program consists of two parts, modul_cashier.py which stores all the functions to run all the program features and main_cashier.py. To use this code, you can run the main_cashier.py in the IDE or you can also run it manually via the command line or CMD depending on the operating system.

## Features
Once the program is running, we can use the features. Here they are:

**1. Add items**
This feature can add item name, item quantity, and item price with one function, namely add_item. The following is a flowchart to explain the working algorithm of this function.

![add_item](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/add_item%20function.drawio.png)

In this feature, the item name input is set with an independent data type (can be a string or float number or integer). This is because an item name can be a number code or string and a number code can also be considered a string. However, when inputting item quantity and item price, the data type is set as float because these two inputs must be numbers and the reason for choosing float is because there is a possibility that the number entered is a fraction. In this feature we need to remember that numbers (float and iteger) can become strings but strings cannot become numbers. As confirmation, conversion to float in the input data can also automatically accommodate the integer data type so that even though our input is an integer it will still be converted to the float data type.

**2. Update input items**
This feature was created to edit items that have been input. In this feature, the process of updating item name, item quantity and item price occurs separately because it uses three different functions.
To update the item name, the function used is update_item_name. The following is a flowchart of the update_item_name function:

![update_item_name](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/update_item_name%20function.drawio.png)

Just like the add_item feature in add name, the update_item_name function can also accept numbers as strings.

To update the item quantity, use the update_item_qty function. Here is the flowchart of update_item_qty:

![update_item_qty](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/update_item_qty%20function.drawio.png)

Next, updating the item price is done using the update_item_price function. Here is the flowchart:

![update_item_price](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/update_item_price%20function.drawio.png)

Just like the add item feature, the update_item_qty and update_item_price functions are also created to accommodate the float data type because there is a possibility that the input data will be decimal.

What is of concern when developing the "Update input item" feature is that when an error occurs in inputting "item name that wants to be updated" and the update you want to make will loop the program again asking for input item name. But when a problem occurs when inputting "new item quantity" and "new item price" the program will loop asking for input "new item quantity" and "new item price"
when we input the strings "update quantity" and "update price".

**3. Delete items**
This feature was created to be able to delete items one by one. The way this feature works is by matching the names of items in the list. When they match, the item will be deleted and the message "The item that wants to be deleted is not listed" will appear when the item is not listed and the program loops again asking for the item you want to delete.

This feature uses the delete_item function from the module. The following is a flowchart of the delete_item algorithm:

![delete_item](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/delete_item%20function.drawio.png)

**4. Reset transactions**
This feature was created to delete all input that has been made so that you can input again from the beginning. This feature is executed using the reset_transaction function from the module. Here is the flowchart:

![reset_transaction](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/reset_transaction%20function.drawio.png)

**5. Check Orders**
In this feature, the error checking process is only based on whether there is an item name input that was not completed. This is because it will collide with the function in the add item and update item features, where these features automatically set the item price and item quantity input in the form of numbers. This is also reinforced by the simultaneous application of the Show transaction feature to several other features so that if an input error occurs it will also fail to display the transaction list.

The Check orders feature is carried out using the check_order function. The following is a flowchart of the check_order function algorithm:

![check_order](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/check_order%20function.drawio.png)


**6. Calculate total purchases**
This feature was created to calculate the total amount that must be paid from all input items made. What's interesting about this feature is that there are discount provisions in the form of:
- 5% for purchases > 200,000
- 8% for purchases > 300,000
- 10% for purchases > 500,000

This feature is executed using the total_paid function from the module. The following is a flowchart of the total_paid function algorithm:

![total_paid](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/total_paid%20function.drawio.png)

**7. Exit**
This feature is executed without a function from the module and is only created by stopping the loop of the running program which only uses the "break" control flow loop in the code.

**8. Show transactions**
This feature is a feature that runs simultaneously when executing several features such as Add item, Update input item, Delete item, Check Orders, and Calculate total purchase. This is so that when running these features you can see details on the list of what has been done.

This feature is executed using the transaction_list function. The flowchart of this feature is as follows:

![transaction_list](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/transaction_list%20function.drawio.png)

## Development

As previously explained, this program is still CLI based so for commercial use it is necessary to build code for the GUI program. Apart from that, it is possible to also develop additional features in the form of input units so that more specific input can be carried out.

On this basis, I am open to input to develop this program. I really hope for suggestions that can direct and teach me how to develop this program.
