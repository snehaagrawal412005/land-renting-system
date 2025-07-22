from read import readData
from operations import display_options, rent_land, return_land

def main():
    print("-" * 100)
    print("\n\t\t\t\t***LANDRENTER***\n")
    print("\t\t\t\tKathmandu\n")
    print("-" * 100)
    print("\nPlease choose the option you want to continue\n")
    print("-" * 100)
    print("Please press 1 to rent")
    print("Please press 2 to return")
    print("Please press 3 to exit\n")

    myDictionary = readData()  # Calling the readData function to get data from data.txt

    while True:
        user_input = input("Please choose among the above options you want to proceed: ")

        if user_input == '1':
            rent_land(myDictionary)
        elif user_input == '2':
            return_land(myDictionary)
        elif user_input == '3':
            print("Thank you for using our system")
            break
        else:
            print("Please enter the correct option (1, 2, or 3)")

if __name__ == "__main__":
    main()
