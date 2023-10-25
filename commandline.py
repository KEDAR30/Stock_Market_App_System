import operations
import json
from json import JSONDecodeError

print("Welcome to Stock Market App")
while(1):
    print("Press: ")
    print("1. Register as Owner")
    print("2. Register as Customer")
    print("3. Login as Owner")
    print("4. Login as Customer")
    print("5. Exit")
    in1 = int(input())
    if in1 == 1:
        print("Enter Username:")
        Username = input()
        print("Full Name:")
        Full_Name = input()
        print("Enter Email ID")
        Email_ID = input()
        print("Enter Password")
        Password = input()
        try:
            f = open('owners.json', 'r')
            content = json.load(f)
            if Username in str(content):
                print("Username already exists !!")
                continue
        except JSONDecodeError:
            pass
        if "@admin.com" not in Email_ID or (len(Email_ID)*len(Username)*len(Password)*len(Full_Name)) == 0 or len(Password) <= 4:
            print("Please Enter Valid Data !!")
            continue
        else:
            operations.Register_Owner(
                'owner', 'Owners.json', Username, Full_Name, Email_ID, Password)
            print("Registered Successully as Owner ")
            continue
    elif in1 == 2:
        print("Enter Username")
        Username = input()
        print("Full Name:")
        Full_Name = input()
        print("Enter Email ID")
        Email_ID = input()
        print("Enter Password")
        Password = input()
        print("Bank Name:")
        Bank_name = input()
        print("Account Balance:")
        Account_balance = int(input())
        if ".com" not in Email_ID or (len(Email_ID)*len(Username)*len(Password)*len(Full_Name)) == 0 or len(Password) <= 4:
            print("Please Enter Valid Data")
            continue
        else:
            operations.Register_Customer(
                'customer', 'Customers.json', Username, Full_Name, Email_ID, Password, Bank_name, Account_balance)
            print("Registered Successully as Customer")
            continue
    elif in1 == 3:
        print("Enter Email_ID")
        Email_ID = input()
        print("Enter Password")
        Password = input()
        ch = operations.Login('owner', 'Customers.json',
                              'Owners.json', Email_ID, Password)
        if ch == True:
            f = open('Owners.json', 'r')
            content = json.load(f)
            owner_details = []
            for i in range(len(content)):
                if content[i]["Email"] == Email_ID and content[i]["Password"] == Password:
                    owner_details.append(content[i])
                    break
            print("Welcome " + str(owner_details[0]["Full Name"]))
            while(1):
                print("Press: ")
                print("1. Create Stock")
                print("2. Update Stock")
                print("3. View all created Stocks")
                print("4. Delete Stock")
                print("5. View Buyer Profile")
                print("6. Logout")
                in2 = int(input())
                if in2 == 1:
                    stock_id = operations.AutoGenerate_StockID()
                    print("Stock ID generated is "+str(stock_id))
                    print("Company Title:")
                    cmp_title = input()
                    print("Stock Name:")
                    Stock_name = input()
                    print("Establishment Year(YYYY):")
                    Establishment_year = input()
                    print("Evaluation:")
                    Evaluation = int(input())
                    print("Enter Price per shares:")
                    Price_per_share = int(input())
                    print("Number of shares:")
                    number_of_shares = int(input())
                    if len(cmp_title)*len(Stock_name) == 0 or Price_per_share <= 0 or number_of_shares <= 0:
                        print("Please enter valid data !!")
                        continue
                    operations.Create_Stock('Stocks.json', stock_id, cmp_title, owner_details[0]["Full Name"], Stock_name,
                                            Establishment_year, Evaluation, Price_per_share, number_of_shares)
                    print("Stock Created Successfully")
                elif in2 == 2:
                    print("Enter Stock ID")
                    stock_id = input()
                    print(
                        "Enter Detail to be updated(Stock Name | Evaluation | Price per share)")
                    Detail_to_be_updated = input()
                    print("Enter Updated detail")
                    if Detail_to_be_updated == 'Price per share':
                        Updated_detail = int(input())
                    else:
                        Updated_detail = input()
                    ch = operations.Update_Stock_Product(
                        'Stocks.json', stock_id, Detail_to_be_updated, Updated_detail)
                    if ch == True:
                        print("Stock updated successfully !!")
                    else:
                        print("Stock not updated !!")
                elif in2 == 3:
                    details = operations.Fetch_all_Stocks_created_by_Owner(
                        owner_details[0]["Full Name"], 'Stocks.json')
                    if len(details) == 0:
                        print("No Stock Created !!")
                    else:
                        print("Stock Details")
                        for i in range(len(details)):
                            print("ID: "+str(details[i]["ID"]))
                            print("Company Title: " +
                                  str(details[i]["Company Title"]))
                            print("Owner: " +
                                  str(details[i]["Owner"]))
                            print("Stock Name: "+str(details[i]["Stock Name"]))
                            print("Establishment Year: " +
                                  str(details[i]["Establishment Year"]))
                            print("Evaluation: "+str(details[i]["Evaluation"]))
                            print("Price per share: " +
                                  str(details[i]["Price per share"]))
                            print("Number of shares: " +
                                  str(details[i]["Number of shares"]))
                            print('\n')
                elif in2 == 4:
                    print("Enter Stock ID: ")
                    st_id = input()
                    dn = operations.Delete_Stock('Stocks.json', st_id)
                    if dn == True:
                        print("Stock Deleted Successfully")
                    else:
                        print("Invalid Stock ID")
                        print("Stock ID: "+str(details[i]["Stock ID"]))
                        print("Company title: " +
                              str(details[i]["Company title"]))
                        print("Owner: " +
                              str(details[i]["Owner"]))
                        print("Stock Name: "+str(details[i]["Stock Name"]))
                        print("Establishment year: " +
                              str(details[i]["Establishment year"]))
                        print("Evaluation: "+str(details[i]["Evaluation"]))
                        print("Price per share: " +
                              str(details[i]["Price per share"]))
                        print("Number of shares: " +
                              str(details[i]["Number of shares"]))
                        print('\n')
                        continue
                elif in2 == 5:
                    print("Enter Username")
                    usrnm = input()
                    details = operations.View_User_Details(
                        'Customers.json', usrnm)
                    if len(details) == 0:
                        print("Invalid Username")
                    else:
                        for i in range(len(details)):
                            print("Account Balance: " +
                                  str(details[i]["Account Balance"]))
                            print("Email: "+str(details[i]["Email"]))
                            print("Cart: ")
                            cart = details[i]["Cart"]
                            for j in range(len(cart)):
                                print("ID: " +
                                      str(cart[j]["ID"]))
                                print("Company Title: " +
                                      str(cart[j]["Company Title"]))
                                print("Quantity: "+str(cart[j]["Quantity"]))
                                print("Total Amount: " +
                                      str(cart[j]["Total Amount"]))
                                print('\n')
                                continue
                elif in2 == 6:
                    break
                else:
                    print("Please Enter valid input")
        else:
            print("Invalid Credentials !!")
    elif in1 == 4:
        print("Enter Email")
        Email_ID = input()
        print("Enter Password")
        Password = input()
        ch = operations.Login('customer', 'Customers.json',
                              'Owners.json', Email_ID, Password)
        if ch == True:
            f = open('Customers.json', 'r')
            content = json.load(f)
            customers_details = []
            for i in range(len(content)):
                if content[i]["Email"] == Email_ID and content[i]["Password"] == Password:
                    customers_details.append(content[i])
            print("Welcome " + str(customers_details[0]["Username"]))
            in3 = 1
            while(in3 != 7):
                print("Press: ")
                print("1. View all Stock")
                print("2. View Stock details by_ID")
                print("3. Manage cart")
                print("4. Place order")
                print("5. Update Profile")
                print("6. View Orders")
                print("7. Logout")
                in3 = int(input())
                if in3 == 1:
                    details = operations.View_all_stocks('Stocks.json')
                    if len(details) == 0:
                        print("No Stock created !!")
                    else:
                        for i in range(len(details)):
                            print("ID: "+str(details[i]["ID"]))
                            print("Company Title: " +
                                  str(details[i]["Company Title"]))
                            print("Owner: " +
                                  str(details[i]["Owner"]))
                            print("Stock Name: "+str(details[i]["Stock Name"]))
                            print("Establishment Year: " +
                                  str(details[i]["Establishment Year"]))
                            print("Evaluation: "+str(details[i]["Evaluation"]))
                            print("Price per share: " +
                                  str(details[i]["Price per share"]))
                            print("Number of shares: " +
                                  str(details[i]["Number of shares"]))
                            print('\n')
                        continue
                elif in3 == 2:
                    print("Enter Stock ID")
                    stock_Id = input()
                    details = operations.View_all_Stocks_by_Id(
                        'Stocks.json', stock_Id)
                    if len(details) == 0:
                        print("Invalid ID")
                    else:
                        for i in range(len(details)):
                            print("ID: "+str(details[i]["ID"]))
                            print("Company Title: " +
                                  str(details[i]["Company Title"]))
                            print("Owner: " +
                                  str(details[i]["Owner"]))
                            print("Stock Name: "+str(details[i]["Stock Name"]))
                            print("Establishment Year: " +
                                  str(details[i]["Establishment Year"]))
                            print("Evaluation: "+str(details[i]["Evaluation"]))
                            print("Price per share: " +
                                  str(details[i]["Price per share"]))
                            print("Number of shares: " +
                                  str(details[i]["Number of shares"]))
                            print('\n')
                elif in3 == 3:
                    print("Press: ")
                    print("1. Add  to cart")
                    print("2. Remove Item from cart")
                    print("3. View Cart")
                    in31 = int(input())
                    if in31 == 1:
                        print("Enter Stock ID")
                        Stock_ID = input()
                        print("Enter Quantity")
                        Quantity = int(input())
                        print("Enter Total cost")
                        f = open('Stocks.json', 'r')
                        try:
                            content = json.load(f)
                            f.close()
                        except JSONDecodeError:
                            print("No Stock created !!")
                            f.close()
                            continue
                        if Stock_ID not in str(content):
                            print("Please Enter Valid Stock ID")
                            continue
                        can_add = operations.Add_item_to_cart(
                            customers_details[0]["Username"], Stock_ID, Quantity, 'Customers.json', 'Stocks.json')
                        f.close()
                        if can_add == True:
                            print("Added item successfully !!")
                            continue
                        else:
                            print("Cannot add item to cart !!")
                            continue
                    if in31 == 2:
                        print("Enter Stock ID")
                        Stock_id = input()
                        f = open('Stocks.json', 'r')
                        try:
                            content = json.load(f)
                            f.close()
                        except JSONDecodeError:
                            print("No Stock created !!")
                            f.close()
                            continue
                        can_remove = operations.Remove_item_from_cart(
                            customers_details[0]["Username"], Stock_id, 'Customers.json')
                        if can_remove == True:
                            print("Item removed successfully from cart !!")
                        else:
                            print("Cannot remove item")
                    elif in31 == 3:
                        cart = operations.View_Cart(
                            customers_details[0]["Username"], 'Customers.json')
                        if len(cart) == 0:
                            print("Cart Empty !!")
                        else:
                            for i in range(len(cart)):
                                print("ID: " +
                                      str(cart[i]["ID"]))
                                print("Company Title: " +
                                      str(cart[i]["Company Title"]))
                                print("Quantity: "+str(cart[i]["Quantity"]))
                                print("Total Amount: " +
                                      str(cart[i]["Total Amount"]))
                                print('\n')
                    else:
                        print("Please Enter Valid choice")
                elif in3 == 4:
                    Order_id = operations.AutoGenerate_OrderID()
                    print("Order ID genrated is "+str(Order_id))
                    order_placed = operations.Place_order(
                        Order_id, customers_details[0]["Username"], 'Customers.json', 'Orders.json', 'Stocks.json')
                    if order_placed == True:
                        print(
                            "Order Placed Successfully with Order ID "+str(Order_id))
                    else:
                        print("Order Unsuccessful !!")
                elif in3 == 5:
                    print(
                        "Enter Detail to be updated ( Email | Password | Account Balance )")
                    Detail_to_be_updated = input()
                    print("Enter Updated detail")
                    if Detail_to_be_updated == "Account Balance":
                        Updated_detail = int(input())
                    else:
                        Updated_detail = input()
                    upd = operations.Update_Customer(
                        'Customers.json', customers_details[0]["Username"], Detail_to_be_updated, Updated_detail)
                    if upd == True:
                        print("Profile Updated successfully !!")
                    else:
                        print("Cannot Update Profile !!")
                elif in3 == 6:
                    orders = operations.View_all_orders(
                        'Orders.json', customers_details[0]["Username"])
                    if len(orders) == 0:
                        print("No orders placed !!")
                    else:
                        for i in range(len(orders)):
                            print("Order ID: "+str(orders[i]["Order ID"]))
                            print("Buyer: " + str(orders[i]["Buyer"]))
                            print("Items: ")
                            cart = orders[i]["Items"]
                            for j in range(len(cart)):
                                print("  ID: " +
                                      str(cart[j]["ID"]))
                                print("  Company Title: " +
                                      str(cart[j]["Company Title"]))
                                print("  Stock Name: " +
                                      str(cart[j]["Stock Name"]))
                                print("  Quantity: "+str(cart[j]["Quantity"]))
                                print("  Total Amount: " +
                                      str(cart[j]["Total Amount"]))
                                print('\n')
                elif in3 == 7:
                    break
                else:
                    print("Please Enter Valid choice")
        else:
            print("Invalid Credentials !!")
    elif in1 == 5:
        break
    else:
        print("Please Enter Valid choice")
