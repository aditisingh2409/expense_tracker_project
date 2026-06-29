

def add_expense():

    amount = input("enter amount:")
#categor 
    category = input("enter category:")
#file open
    with open("expense.txt" , "a") as file:
        file.write(f"{amount},{category}\n")

#successmessage
        print("expense added succesfully")

add_expense()

def view_expenses():  

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
