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
                with open("D:\GitHub\Smart-Shop-Billing-System\prod_list.txt", "a") as f:
                  f.write(f"{name}|{price}\n")
                print("Product added successfully....✅\n")

            elif choice==3:
                show_prod
                remove_prod=""
                id=input("Enter the name of product  to remove from product list")
                with open("D:\GitHub\Smart-Shop-Billing-System\prod_list.txt") as f:
                 for line in f:
                  prod,price = line.strip().split("|")
                  if prod==id:
                    remove_prod= prod
                    break
                try:
                    with open("D:\GitHub\Smart-Shop-Billing-System\prod_list.txt", "r") as file:
                       lines = file.readlines()
                    with open("D:\GitHub\Smart-Shop-Billing-System\prod_list.txt", "w") as file:
                      for line in lines:
                        if line != remove_prod:
                            file.write(line) 
                except FileNotFoundError:
                    print("Product not found")

            elif choice==4:
                break
            else:
                print("Enterd Invalid Choise")

    else:
        print("Invalid Login")
#elif ch==2:
else:
    print("Entered invalid choise")

