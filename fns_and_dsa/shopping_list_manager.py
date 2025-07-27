# shopping_list_tool.py

shopping_list = []

def display_menu():
    print("\nShopping List Menu:")
    print("1. View shopping list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            print("\nYour Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
        elif choice == 2:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the list.")
        elif choice == 3:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print(f"{item} not found in the list.")
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Please choose a valid option (1-4).")

if __name__ == "__main__":
    main()