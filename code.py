#Smart Shop Billing system

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
                print(f"{prod}\t{price}")
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
    




