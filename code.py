#Smart Shop Billing system
import qrcode

#bill qr generating function
def generate_qr(amount):
    upi_id = "pathakashutosh679@okaxis"  
    name = "SmartShop"

    upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

    qr = qrcode.QRCode()
    qr.add_data(upi_url)
    qr.make()

    print("\nScan this QR to pay:\n")
    qr.print_ascii()


print("Welcome to Smart Shop🛒\n")
print("Press 1 for owner Dashboard\nPress 2 for costumer Dashboard\n")

ch=int(input())

#Function to show products
def show_prod():
    print("\nProduct\t\tPrice")
    try:
        with open(r"D:\GitHub\Smart-Shop-Billing-System\prod_list.txt") as f:
            for line in f:
                prod,price = line.strip().split("|")
                print(f"{prod}\t\t{price}")
    except FileNotFoundError:
        print("Product file not found")

#Owner Dashboard

if ch==1:
    password=input("Enter the password for owner login🧐 :")

    if password=="owner123":
        print("\nOwner Dashboard")
        print("-----------------")

        while(True):
            print("\nPress 1 to show Product list ")
            print("Press 2 to add new Product")
            print("Press 3 to remove Product")
            print("Press 4 to Exit :")

            choice=int(input())

            #Show Products
            if choice==1:
                show_prod()

            #Add Product
            elif choice==2:

                name=input("Enter the Product name :")
                price=float(input("Enter the price of the product :"))

                with open(r"D:\GitHub\Smart-Shop-Billing-System\prod_list.txt", "a") as f:
                  f.write(f"{name}|{price}\n")

                print("Product added successfully....✅\n")

            #Remove Product
            elif choice==3:
                show_prod()

                remove_prod = ""
                id=input("Enter the name of product  to remove from product list")

                try:
                    with open(r"D:\GitHub\Smart-Shop-Billing-System\prod_list.txt", "r") as file:
                       lines = file.readlines()

                    with open(r"D:\GitHub\Smart-Shop-Billing-System\prod_list.txt", "w") as file:
                        
                        for line in lines:
                            prod, price = line.strip().split("|")
                           
                            if prod.lower() != id.lower():   # case-insensitive match
                                file.write(line)
                            
                            else:
                                remove_prod = prod
                   
                    if remove_prod == "":
                        print("Product not found ❌")
                    
                    else:
                        print(f"{remove_prod} removed successfully ✅")
                
                except FileNotFoundError:
                    print("File not found")

            #Exit Owner Dashboard        
            elif choice==4:
                break

            #Invalid Choise
            else:
                print("Enterd Invalid Choise")
    
    #Invalid Login
    else:
        print("Invalid Login")

#Costumer Dashboard
elif ch==2:
    print("\n🛒Costumer Dashboard🛒")
    print("------------------------\n")

    print("---Available Products---")
    print("------------------------")
    show_prod()

    #Show costumer cart function
    def show_cart():
        print("\nProduct\t\tPrice\t\tQuantity\t\tTotal")

        try:
        
            with open(r"D:\GitHub\Smart-Shop-Billing-System\cart.txt") as f:
        
                for line in f:
                    prod,price,quan,tot = line.strip().split("|")
                    print(f"{prod}\t\t{price}\t\t{quan}\t\t{tot}")
        
        except FileNotFoundError:
            print("Product file not found")


    while(True):

        print("\nPress 1 to View your Cart")
        print("Press 2 to Add Product")
        print("Press 3 to Remove Product")
        print("Press 4 to Generate bill")
        print("Press any other key to exit")

        ch=int(input())

        #show cart
        if ch==1:
            show_cart()
        
        #Add Produt to cart
        elif ch==2:

            name=input("Enter the name of the product to add in cart")
            quant=int(input("Enter the quantity :"))

            try:
                found = False
                with open(r"D:\GitHub\Smart-Shop-Billing-System\prod_list.txt") as f:
                   
                   for line in f:
                      prod,price = line.strip().split("|")

                      if prod.lower() == name.lower():
                          price = float(price)
                          total = price * quant

                          with open("D:\GitHub\Smart-Shop-Billing-System\cart.txt","a") as f:
                              f.write(f"{prod}|{price}|{quant}|{total}\n")

                          print("Product Added Successfully....✅")
                          found = True
                          break
               
                if not found:
                    print("Product not found....❌")
           
            except FileNotFoundError:
                print("Product file missing..🔍")

        #Remove from Cart
        elif ch==3:

            show_cart()
            remove_prod = ""

            name=input("\nEnter the name of the product to remove from the cart :")
            
            try:
                with open(r"D:\GitHub\Smart-Shop-Billing-System\cart.txt", "r") as file:
                    lines = file.readlines()

                with open(r"D:\GitHub\Smart-Shop-Billing-System\cart.txt", "w") as file:
                    for line in lines:
                        prod, price, quant, tot = line.strip().split("|")

                        if prod.lower() != name.lower(): #case sensitive match
                            file.write(line)
                        else:
                            remove_prod = prod

                    if remove_prod == "":
                        print("Product not found in the cart ❌")
                    else:
                        print(f"{remove_prod} removed successfully from the cart ✅")
            except FileNotFoundError:
                print("Cart file not found") 
        
        elif ch==4:
            print("\nSmart Shop 🏪\nTotal Bill 📜")
            print("--------------------")
            total_bill = 0
            try:
                with open(r"D:\GitHub\Smart-Shop-Billing-System\cart.txt") as f:
                    
                    for line in f:
                        
                        prod, price, quant, tot = line.strip().split("|")
                        total_bill += float(tot)
                        
                    gst = total_bill * 0.18
                    final_bill = total_bill + gst
                    
                    show_cart()
                    print("_______________________________________________________________________")
                    print("Total Amount\t\t\t\t\t",total_bill)
                    print("GST (18%)\t\t\t\t\t",gst)
                    print("Final Amount\t\t\t\t\t",final_bill)
                    generate_qr(final_bill)

            except FileNotFoundError:
                print("Cart is empty...🛒")
        
        #Exit costumer dashboard
        else:
            break



        

                    

                      









