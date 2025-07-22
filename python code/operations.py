from write import write_invoice

# variable to store rental details
user_land = []

def get_rental_details(kitta_number):
    for item in user_land:
        if item[0] == kitta_number:
            return item
    return None

def display_options():# to choose if we wnat to rent, return, exit.
    print("-" * 100)
    print("\n\t\t\t\t**LANDRENTER**\n")
    print("\t\t\t\tKathmandu\n")
    print("-" * 100)
    print("\nPlease choose the option you want to continue\n")
    print("-" * 100)
    print("Please press 1 to rent")
    print("Please press 2 to return")
    print("Please press 3 to exit\n")

def rent_land(myDictionary):
    print("Thank you for renting our land")
    name = input("Please enter your name: ")
    contact_no = input("Please enter your contact number: ")
    
    print("\nBelow are the available options:\n")
    print("-" * 100)
    print("Kitta num\t District \t Direction \t Aana \t Price \t Availability")
    print("-" * 100)

    kitta_num = 101
    for kitta_number in myDictionary.keys():
        print(str(kitta_num) + "\t" + myDictionary[kitta_number][0] + "\t" + myDictionary[kitta_number][1] + "\t" + myDictionary[kitta_number][2] + "\t" + myDictionary[kitta_number][3] + "\t" + myDictionary[kitta_number][4])
        kitta_num += 1

    current_rentals = []# Creating a temporary list to store rental details for the current invoice.

    while True:
        try:
            kitta_number = int(input("\nPlease enter the kitta number from the list above: "))
            
            if kitta_number <= 100 or kitta_number > len(myDictionary) + 100:
                print("Please enter a correct kitta number.")
                continue
            
            aana_land = int(myDictionary[kitta_number][2])
            print(str(kitta_number) + " kitta has " + str(aana_land) + " aana of land")
            month = int(input("Please enter the number of months you want to rent for: "))
            land_price_per_month = int(myDictionary[kitta_number][3])

            total_price = month * land_price_per_month

            
            current_rentals.append([kitta_number, aana_land, month, land_price_per_month, total_price])# Store the rental details in the above temprorary list.

            myDictionary[kitta_number][4] = "Not Available"  # Changing the availability status.
            
            more = input("\nDo you want to rent more? (yes/no): ").lower()#changes Yes to yes and No to no so that input error doesnot occur.
            if more != 'yes':
                print("-" * 100)
                print("\nInvoice:\n")
                print("\t \t \t \t \t LANDRENTER\n")
                print("\t \t \t Address: Kamalpokhari Kathmandu Metropolitian\n")
                print("\t\t\t Contact no: 9817976507 || Email: snehaagrawal41@gmail.com\n")
                print("Name of the customer: " + name + "\n")
                print("Phone of the customer: " + contact_no + "\n")
                print("-" * 100)
                print("\t\t\t Kitta num\t District \t Direction \t Aana \t Price \t Totalprice\n")
                print("-" * 100)

                for item in current_rentals: #printing the temprorary list.
                    print("\t\t\t" + str(item[0]) + "\t" + myDictionary[item[0]][0] + "\t" + myDictionary[item[0]][1] + "\t" + str(item[1]) + "\t" + str(item[3]) + "\t" + str(item[4]))

                print("\nTotal amount is " + str(sum(item[4] for item in current_rentals)))
                print("Thank you for using LANDRENTER\n")

                # Call function to write invoice to file
                write_invoice(name, contact_no, current_rentals, myDictionary)

               
                user_land.extend(current_rentals) # Append temprorary list to user_land
                
                break

        except (ValueError, KeyError):
            print("Invalid input for kitta number or months. Please enter numeric values.")

def return_land(myDictionary):
    print("Thank you for returning our land")
    name = input("Please enter your name: ")
    contact_no = input("Please enter your contact number: ")

    while True:
        try:
            kitta_number = int(input("Please enter the kitta number of the land you want to return: "))
            
            if kitta_number <= 100 or kitta_number > len(myDictionary) + 100:
                print("Please enter a correct kitta number.")
                continue

            # Retrieving the rental details calling this function
            rental_details = get_rental_details(kitta_number)
            if rental_details:
                kitta_number, aana_land, months_rented, land_price_per_month, total_price = rental_details
            else:
                print("This kitta number was not rented or does not match any records.")
                
                print("Cannot process the return for this kitta number.")
                break

            
            months_returned = int(input("Please enter the number of months after which you are returning this land: ")) 
            
            fine = (months_returned - months_rented) * 1000 #calculating fine

            if fine < 0:
                fine = 0  # Setting fine to 0 if it's negative since negetive means land was returnrd early.

            print("You will be fined " + str(fine) + ".")

            myDictionary[kitta_number][4] = "Available"  # Changing the availability status

            return_details = [
                [kitta_number, aana_land, months_rented, land_price_per_month, fine]   #Preparing the return invoice details.
            ]

            # Call function to write invoice to file, including return details
            write_invoice(name, contact_no, return_details, myDictionary, receipt_type="return")

            print("-" * 100)
            print("\nReturn Receipt:\n")
            print("\t \t \t \t \t LANDRENTER\n")
            print("\t \t \t Address: Kamalpokhari Kathmandu Metropolitian\n")
            print("\t\t\t Contact no: 9817976507 || Email: snehaagrawal41@gmail.com\n")
            print("Name of the customer: " + name + "\n")
            print("Phone of the customer: " + contact_no + "\n")
            print("-" * 100)
            print("\t\t\t Kitta num\t District \t Direction \t Aana \t Price \t Fine\n")
            print("-" * 100)
            print("\t\t\t" + str(kitta_number) + "\t" + myDictionary[kitta_number][0] + "\t" + myDictionary[kitta_number][1] + "\t" + str(aana_land) + "\t" + str(land_price_per_month) + "\t" + str(fine))

            print("\nTotal fine is " + str(fine))
            print("Thank you for using LANDRENTER\n")

            break

        except (ValueError, KeyError):
            print("Invalid input for kitta number or months. Please enter numeric values.")

