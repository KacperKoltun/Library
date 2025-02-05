import webbrowser as wb

def main():
    choice = 0
    while choice != 4:
        print("Choose an option:")
        print("1. Yes")
        print("2. No")
        print("3. Maybe")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice == 1:
            wb.open("https://www.youtube.com/watch?v=bmfudW7rbG0&list=RDbmfudW7rbG0&start_radio=1&rv=XxAB9BAxpJw")
        elif choice == 2:
            print("You chose No")
        elif choice == 3:
            print("You chose Maybe")
        elif choice == 4:
            print("Exiting...")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()