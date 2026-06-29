#ek fun create kr rhe h jiska nam add expense hai 

def add_expense():
    #input lwnge ab iska mtlb usr se amoun5 lena hain 
    amount = input("enter amount:")
#categori lena 
    category = input("enter category:")
#file open krna 
    with open("expense.txt" , "a") as file:
        file.write(f"{amount},{category}\n")

#successmessage
        print("expense added succesfully")

add_expense()

def view_expenses(): #file m jo bhi expense h vo show krta hain
    #add expense = fun. ko chala5a hain and view wxpwnse dusra fun chala5b hain 

    with open("expense.txt", "r") as file:

        data = file.readlines()

        print("\nAll expense:")

        for expense in data :
            print(expense.strip())
            
while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Thanks!!")
        break
    else:
        print("Invalid choice")
