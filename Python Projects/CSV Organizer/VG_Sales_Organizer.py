#Nick Caravaggio
# CSV Organizer Example

import tkinter as tk

#Importing 100 records from csv file
file_name = "Video_Games_Sales_as_at_22_Dec_2016.csv"
file_object = open(file_name, "r")
#Declaring primary use lists
game_records = []
game_record_column_headers = []
categories = {}
counter = 0
version = "1.0"

#list order being assigned to names for easier access
name = 0
platform = 1
year_of_release = 2
genre = 3
publisher = 4
NA_sales = 5
EU_sales = 6
JP_sales = 7
other_sales = 8
global_sales = 9
critic_score = 10
critic_count = 11
user_score = 12
user_count = 13
developer = 14
rating = 15

#For loop appends all data to game_records
for line in file_object:
    row = line.split(",")
    if counter == 0:
        game_record_column_headers = row
    #elif statement to decrease output to 20, for faster testing.
    #elif counter == 20:
        #break
    else:
        game_records.append(row)
    counter += 1

#function High_Critic_Score asks user for minimum score, returns list of games
#with a critic score above that input.
def high_critic_score():
    minimum_score = int(input("Enter minimum score: "))
    for items in game_records:
        #Ignores games where no critic score is reported.
        if items[critic_score] == '':
            pass
        elif float(items[critic_score]) > float(minimum_score):
            print("Name:", items[name], "| Score:", items[critic_score])

#Function sort_platform() asks user for a platform, or will list all available
#platforms if the user types !help
def sort_platform():
    the_platform = input("Enter platform ('!help' for examples): ")
    if the_platform == "!help":
        print("Examples: 3DS, DS, GBA, N64, PC, PS, PS2, PS3, PS4,"\
              " SNES, X360, XB")
        sort_platform()
    else:
        print("------------------\nGames on: ", the_platform,\
              "\n------------------")
        for items in game_records:
            if items[platform] == the_platform:
                print(items[name])

#Function sort_publisher asks user for a platform, or will list all available
#publishers if the user types !help
def sort_publisher():
    the_publisher = input("Enter publisher ('!help' for examples): ")
    if the_publisher == "!help":
        print("Examples: Activision, Nintendo, Sony Computer Entertainment,"\
              "Ubisoft, etc.")
        sort_publisher()
    else:
        print("------------------\nGames from: ", the_publisher,\
              "\n------------------")
        for items in game_records:
            if items[publisher] == the_publisher:
                print(items[name])

#Function to ask user for minimum amount of copies sold.
def ask_for_sales():
    return float(input("Enter minimum copies sold (in millions): "))

#function high_sales() will ask user which region they'd like to see sales
#higher than their minimum inputted number.
def high_sales():
    region = input("Which region would you like to see minimum copies sold"\
                    " in? \n(!help for options): ")
    if region == "!help":
        print("Region Options: 'NA', 'EU', 'JP', 'Other', or 'Global'. "\
              "(Note: Case-sensitive.)")
        high_sales()
    elif region == "NA":
        minimum_sales = ask_for_sales()
        for items in game_records:
            if float(items[NA_sales]) > minimum_sales:
                print("Name:", items[name], "| "\
                      "Copies Sold:", items[NA_sales])
    elif region == "EU":
        minimum_sales = ask_for_sales()
        for items in game_records:
            if float(items[EU_sales]) > minimum_sales:
                print("Name:", items[name], "| "\
                      "Copies Sold:", items[EU_sales])
    elif region == "JP":
        minimum_sales = ask_for_sales()
        for items in game_records:
            if float(items[JP_sales]) > minimum_sales:
                print("Name:", items[name], "| "\
                      "Copies Sold:", items[JP_sales])
    elif region == "Other":
        minimum_sales = ask_for_sales()
        for items in game_records:
            if float(items[other_sales]) > minimum_sales:
                print("Name:", items[name], "| "\
                      "Copies Sold:", items[other_sales])
    elif region == "Global":
        minimum_sales = ask_for_sales()
        for items in game_records:
            if float(items[global_sales]) > minimum_sales:
                print("Name:", items[name], "| "\
                      "Copies Sold:", items[global_sales])
    else:
        print("ERROR: Not a valid region.")
        high_sales()

def print_available_functions():
    print("------------------\n"\
          "Programs Available as of Version", version, "\n"\
          "1. Sort by Game's minimum Critic Score (scale 1-100)\n"\
          "2. Sort by Game's Platform (ex. Xbox, PS3, etc.)\n"\
          "3. Sort by Game's Publisher (ex. Activision, EA, Nintendo)\n"\
          "4. Sort by Game's minimum copies sold (in millions)")

#default program that runs
def default():
    choice = input("------------------\n"\
                   "What would you like to do now? \n"\
                   "(Type function #, !help, or !end): ")
    if choice == "!help":
        print_available_functions()
        default()
    elif choice == "1":
        high_critic_score()
        default()
    elif choice == "2":
        sort_platform()
        default()
    elif choice == "3":
        sort_publisher()
        default()
    elif choice == "4":
        high_sales()
        default()
    elif choice == "!end":
        print("------------------\n"\
              "Thank you for using Nick's video game sales data sorting"\
              " program!\nHave a nice day :)")
    else:
        print("That is not a function or command.")
        default()
    
if __name__ == "__main__":
    print("Hi! Welcome to Nick's video game sales data sorting program!")
    print_available_functions()
    default()
