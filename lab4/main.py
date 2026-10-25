# P2. Create an application that manages tennis players. Each player is characterized by:
# name (str), nationality (str), ATP ranking points (int, e.g. 8535), number of tournaments won (int). The application
# should provide the following feature
from ui import *

# MAIN FUNCTION
def main():
    while True:
        application()
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            add_player_ui()

        if option == 2:
            modify_player_ui()

        if option == 3:
            show_list()

        if option == 4:
            remove_player_nat_ui()

        if option == 5:
            remove_player_by_pts_ui()

        if option == 6:
            display_players_based_if_divide_ui()

        if option == 7:
            display_by_greater_number_ui()

        if option == 8:
            display_by_less_number_ui()

        if option == 9:
            win_country_ui()

        if option == 10:
            how_many_players_ui()

        if option == 11:
            substring_search_ui()

        if option == 12:
            podium_ui()




main()



