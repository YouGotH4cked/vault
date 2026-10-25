from service import *
from domain import *
from infrastructure import *


def application():
    print("\n")
    print(" Tennis Player Management Application")
    print("--------------------------------------")
    print("1. Add a new player")
    print("2. Modify an existing player")
    print("3. Show the list of players")
    print("4. Remove players from a given country")
    print("5. Remove players with ATP ranking points in a given interval")
    print("6. Display players from a given country whose ATP ranking points are divisible by a given number")
    print("7. Display players from a given country whose ATP ranking points are greater than a given number")
    print("8. Display players with a given number of tournaments won whose ATP ranking points are less than a given number")
    print("9. Display the total number of tournaments won by players from a given country")
    print("10. Display the number of players from each country")
    print("11. Display players whose name contains a given substring, sorted in descending order by ATP ranking points")
    print("12. Display the top 3 players with the highest ATP ranking points, sorted in descending order by the number of tournaments won")
    print("--------------------------------------")


def add_player_ui():
    try:
        name = input("Enter the player's name: ")
        nationality = input("Enter the player's nationality: ")
        ranking_points = int(input("Enter the player's ATP ranking points: "))
        tournaments_won = int(input("Enter the number of tournaments won by the player: "))

        add_player_s(name, nationality, ranking_points, tournaments_won)
        print("Player added successfully")
    except ValueError as e:
        print(f"\n[ERROR] Invalid data: {e}")
        print("The operation was canceled. Please try again from the menu.")


def modify_player_ui():
    mod_name = input("Enter the name of the player to modify: ")
    modify_player_s(mod_name)


def show_list():
    for i , player in enumerate(players_list):
        print(f"{i+1}. {player['name']}, {player['nationality']}, {player['ranking_points']}, {player['tournaments_won']}")


# REMOVAL FUNCTIONS
def remove_player_nat_ui():
    country = input("Enter the nationality of the players to remove: ")
    remove_player_nat_s(country)
    print(f"Players from {country} have been removed.")


def remove_player_by_pts_ui():
    try:
        min_points = int(input("Enter the minimum ATP ranking points: "))
        max_points = int(input("Enter the maximum ATP ranking points: "))
        check_min_max_points(min_points, max_points)
    except ValueError as e:
        print(f"\n[ERROR] Invalid data: {e}")
        print("The operation was canceled. Please try again from the menu.")
        return

    remove_player_by_pts_s(min_points, max_points)
    print(f"Players with ATP ranking points between {min_points} and {max_points} have been removed.")


# DISPLAY FUNCTIONS
def display_players_based_if_divide_ui():
    country = input("Enter a country: ")
    try:
        div = int(input("Enter a number to divide the ATP ranking points: "))
        display_players_based_if_divide_s(country, div)
    except ValueError as e:
        print(f"\n[ERROR] Invalid data: {e}")
        print("The operation was canceled. Please try again from the menu.")
        return


def display_by_greater_number_ui():
    country = input("Enter a country: ")
    try:
        greater_number = int(input("Enter the greater number: "))
        display_by_greater_number_s(country, greater_number)
    except ValueError  as e:
        print(f"\n[ERROR] Invalid data: {e}")
        print("The operation was canceled. Please try again from the menu.")
        return


def display_by_less_number_ui():
    try:
        wins = int(input("Enter the number of tournaments won: "))
        less_number = int(input("Enter the lesser number: "))
        display_by_less_number_s(wins, less_number)
    except ValueError as e:
        print(f"\n[ERROR] Invalid data: {e}")
        print("The operation was canceled. Please try again from the menu.")
        return


# REPORTS
def win_country_ui():
    country = input("Enter the country: ")
    count = win_country_s(country)
    if count == 0:
        print(f"No tournaments record of players from {country}.")
    else:
        print(f"The total number of tournaments won by players from {country} is {count}")

def how_many_players_ui():
    if not players_list:
        print("No players in the list.")
        return


    players_country = how_many_players_s()
    print("Number of players from each country:")
    for country, count in players_country.items():
        print(f"{country}: {count} players")


def substring_search_ui():
    substring = input("Enter the substring to search: ")
    players_substr = substring_search_s(substring)
    if not players_substr:
        print(f"No players found with the substring '{substring}' in their name.")
    else:
        print(f"Players with the substring '{substring}' in their name (sorted by ATP ranking points):")
        for player in players_substr:
            print(f"{player['name']}, {player['nationality']}, {player['ranking_points']}, {player['tournaments_won']}")

def podium_ui():
    if len(players_list) < 3:
        print("Not enough players")
        return

    podium = podium_s()
    print("Top 3 players:")
    for i, player in enumerate(podium):
        print(f"{i+1}. {player['name']},  {player['tournaments_won']}")


# UNDO
def undo_last_action():
    undo_last_action_s()
    print("Last action has been undone successfully.")
