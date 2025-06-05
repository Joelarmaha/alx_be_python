def shopping_list():
    shopping_list = []

    while True:
        print("\nShopping List Menu:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View list")
        print("4. Exit")

        operation = input("Enter your choice (1/2/3/4): ")

        if operation == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to the list.")

        elif operation == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif operation == '3':
            print("Your shopping list:")
            for item in shopping_list:
                print("-", item)

        elif operation == '4':
            print("Exiting the shopping list program.")
            break

        else:
            print("Invalid choice, please try again.")
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()