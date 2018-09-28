'''u
Created on Sep 26, 2018

@author: abandari22
'''

name = input("Please enter your name:")
number = input("Enter your phone number:")
product = input("Please enter the name of the product you want to purchase:")
price =  float(input("Enter the price of the item:"))
quantity = int(input("Quantity:"))
subtotal = (price*quantity)
tax = ((0.06)*subtotal)
total =(subtotal+tax)
print(name)
print(number)
print("Purchase information:")
print(product,"    ","Qty:", quantity,"     ","Price:", price)
print("Subtotal:$", subtotal, "  Tax:$", tax,"  Total:$", total)
