#Smart Shop Billing system

print("Welcome to Smart Shop")
print("Press 1 for owner Dashboard\nPress 2 for costumer Dashboard\n")
ch=int(input())
if ch==1:
    password=input("Enter the password for owner login :")
    if password=="owner123":
        print("\nOwner Dashboard")
        print("-----------------")
        while(True):
            print("Press 1 to show Product list\nPress 2 to add new Product\nPress 3 to remove Product\nPress 4 to Exit :")
            choice=int(input())
            if choice==1:
                show_prod()
            elif choice==2:
                name=input("Enter the Product name :")
                price=float(input("Enter the price of the product :"))

            elif choice==3:
                id=int(input("Enter the product id to remove from product list"))
            elif choice==4:
                break
            else:
                print("Enterd Invalid Choise")

    else:
        print("Invalid Login")
elif ch==2:
else:
    print("Entered invalid choise")