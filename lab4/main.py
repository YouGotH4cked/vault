# P2. Create an application that manages tennis players. Each player is characterized by:
# name (str), nationality (str), ATP ranking points (int, e.g. 8535), number of tournaments won (int). The application
# should provide the following feature

players_list = []

def aplication():
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
    print("9. Exit the application")
    print("--------------------------------------")

def show_list(players_list):
    for i , player in enumerate(players_list):
        print(f"{i+1}. {player['name']}, {player['nationality']}, {player['ranking_points']}, {player['tournaments_won']}")

# ADD AND MODIFY FUNCTIONS
def add_player(players_list):
    name = input("Enter the player's name: ")
    nationality = input("Enter the player's nationality: ")
    ranking_points = int(input("Enter the player's ATP ranking points: "))
    tournaments_won = int(input("Enter the number of tournaments won by the player: "))

    player = {
        "name" : name,
        "nationality" : nationality,
        "ranking_points" : ranking_points,
        "tournaments_won" : tournaments_won
    }
    players_list.append(player)

def modify_player(players_list, mod_name):
    for player in players_list:
        if player["name"] == mod_name:
            print(f"Modifying player: {mod_name}")
            player["ranking_points"] = int(input("Enter the new ATP ranking points: "))
            player["tournaments_won"] = int(input("Enter the new number of tournaments won: "))
            print("Player information updated successfully.")
            return
    print(f"Player with name {mod_name} not found.")

# REMOVAL FUNCTIONS
def remove_player_nat(players_list, country):
    new_list = []

    for player in players_list:
        if player["nationality"] != country:
            new_list.append(player)

    players_list.clear()
    players_list.extend(new_list)

    print(f"Players from {country} have been removed.")


def remove_player_pts(players_list, min_points, max_points):
    new_list = []

    for player in players_list:
        if player["ranking_points"] < min_points or player["ranking_points"] > max_points:
            new_list.append(player)

    players_list.clear()
    players_list.extend(new_list)

    print(f"Players with ATP ranking points between {min_points} and {max_points} have been removed.")

# DISPLAY FUNCTIONS
def display_players_based_if_divide(players_list, country, div):
    for player in players_list:
        if player["ranking_points"] % div == 0 and player["nationality"] == country:
            print(f"{player['name']}, {player['nationality']}, {player['ranking_points']}, {player['tournaments_won']}")

def display_by_greater_number(players_list, country, greater_number):
    for player in players_list:
        if player["ranking_points"] > greater_number and player["nationality"] == country:
            print(f"{player['name']}, {player['nationality']}, {player['ranking_points']}, {player['tournaments_won']}")

def display_by_less_number(players_list, wins, less_number):
    for player in players_list:
        if player["ranking_points"] < less_number and player["tournaments_won"] == wins:
            print(f"{player['name']}, {player['nationality']}, {player['ranking_points']}, {player['tournaments_won']}")


# MAIN FUNCTION
def main():
    while True:
        aplication()
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            add_player(players_list)

        if option == 2:
            mod_name = input("Enter the name of the player to modify: ")
            modify_player(players_list, mod_name)

        if option == 3:
            show_list(players_list)

        if option == 4:
            country = input("Enter the nationality of the players to remove: ")
            remove_player_nat(players_list, country)

        if option == 5:
            min_points = int(input("Enter the minimum ATP ranking points: "))
            max_points = int(input("Enter the maximum ATP ranking points: "))
            remove_player_pts(players_list, min_points, max_points)

        if option == 6:
            country = input("Enter the given country: ")
            div = int(input("Enter the number you want to divide the ATP ranking points with: "))
            display_players_based_if_divide(players_list, country, div)

        if option == 7:
            country = input("Enter the given country: ")
            greater_number = int(input("Enter the number of greater points: "))
            display_by_greater_number(players_list, country, greater_number)

        if option == 8:
            wins = int(input("Enter the number of won tournaments: "))
            less_number = int(input("Enter the number of lesser points: "))
            display_by_less_number(players_list, wins, less_number)

        if option == 9:
            break


main()



