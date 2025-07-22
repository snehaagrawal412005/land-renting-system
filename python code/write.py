from datetime import datetime

def write_invoice(name, contact_no, user_land, myDictionary, receipt_type="rental"):
    today_date_and_time = datetime.now().strftime("%d_%m_%y_%H_%M_%S")

    with open(f"{name}_{contact_no}_{today_date_and_time}_{receipt_type}.txt", 'w+') as file:
        file.write("\n")
        file.write("\t \t \t \t \t ***LANDRENTER***")
        file.write("\n")
        file.write("\t \t \tAddress: Kamalpokhari Kathmandu Metropolitian")
        file.write("\n")
        file.write("\t\t\tContact: 9817976507 || Email: snehaagrawal41@gmail.com")
        file.write("\n")
        file.write("Name of the customer:" + name + "\n")

        file.write("----------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        if receipt_type == "return":
            file.write("\t\t\tKitta\tAana\tMonths\tPrice/Month\tFine")
        else:
            file.write("\t\t\tKitta\tAana\tMonths\tPrice/Month\tTotal Price")
        file.write("\n")
        file.write("----------------------------------------------------------------------------------------------------------------------")
        file.write("\n")

        for i in user_land:
            if receipt_type == "return":
                file.write("\t\t\t" + str(i[0]) + "\t\t" + str(i[1]) + "\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t" + str(i[4]))
            else:
                file.write("\t\t\t" + str(i[0]) + "\t\t" + str(i[1]) + "\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t" + str(i[4]))
            file.write("\n")

        if receipt_type == "return":
            total_fine = sum(item[4] for item in user_land)
            file.write("\nTotal fine is " + str(total_fine))
        else:
            total_price = sum(item[4] for item in user_land)
            file.write("\nTotal amount is " + str(total_price))
        
        file.write("\nThank you for using LANDRENTER")
