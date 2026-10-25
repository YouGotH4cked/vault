from domain import create_player, check_div, get_points, get_tourneys
from infrastructure import *


def add_player_s(name, nationality, ranking_points, tournaments_won):
    player = create_player(name, nationality, ranking_points, tournaments_won)

    players_list.append(player)

def modify_player_s(name):
    for player in players_list:
        if player["name"] == name:
            while True:
                try:
                    new_points = int(input("Enter new points: "))
                    if new_points < player["ranking_points"]:
                        print(f"Error: New points cannot be less than current points!")
                    else:
                        break
                except ValueError:
                    print("Error: Please enter a valid integer number!")

            while True:
                try:
                    new_tournaments = int(input("Enter new number of tournaments won: "))
                    if new_tournaments < player["tournaments_won"]:
                        print(
                            f"Error: New number cannot be less than current tournaments!")
                    else:
                        break
                except ValueError:
                    print("Error: Please enter a valid integer number!")

            player["ranking_points"] = new_points
            player["tournaments_won"] = new_tournaments
            print("Player information updated successfully.")
            return

    print(f"Player with name {name} not found.")

# REMOVAL FUNCTIONS
def remove_player_nat_s(country):
    new_list = []

    for player in players_list:
        if player["nationality"] != country:
            new_list.append(player)

    players_list.clear()
    players_list.extend(new_list)


def remove_player_by_pts_s(min_points, max_points):
    new_list = []

    for player in players_list:
        if player["ranking_points"] < min_points or player["ranking_points"] > max_points:
            new_list.append(player)

    players_list.clear()
    players_list.extend(new_list)

# DISPLAY FUNCTIONS
def display_players_based_if_divide_s(country, div):
    check_div(div)

    for player in players_list:
        if player["nationality"] == country and player["ranking_points"] % div == 0:
            print(f"{player['name']}, {player['nationality']}, {player['ranking_points']}, {player['tournaments_won']}")


def display_by_greater_number_s(country, greater_number):
    for player in players_list:
        if player["ranking_points"] > greater_number and player["nationality"] == country:
            print(f"{player['name']}, {player['nationality']}, {player['ranking_points']}, {player['tournaments_won']}")


def display_by_less_number_s(wins, less_number):
    for player in players_list:
        if player["ranking_points"] < less_number and player["tournaments_won"] == wins:
            print(f"{player['name']}, {player['nationality']}, {player['ranking_points']}, {player['tournaments_won']}")


# REPORTS
def win_country_s(country):
    count = 0
    for player in players_list:
        if player["nationality"] == country:
            count += player["tournaments_won"]

    return count


def how_many_players_s():
    players_country = {}
    for players in players_list:
        country = players["nationality"]
        if country in players_country:
            players_country[country] += 1
        else:
            players_country[country] = 1
    return players_country


def substring_search_s(substring):
    players_substr = []
    for players in players_list:
        if substring.lower() in players["name"].lower():
            players_substr.append(players)

    players_substr.sort(key=get_points, reverse=True)
    return players_substr


def podium_s():
    sorted_players = []
    for players in players_list:
        sorted_players.append(players)

    sorted_players.sort(key=get_points, reverse=True)
    top3 = sorted_players[:3]
    top3.sort(key=get_tourneys, reverse=True)

    return top3

# UNDO FUNCTION
def undo_last_action_s():
    if len(history) == 0:
        print("No actions to undo.")
        return

    players_list.clear()
    players_list.extend(history.pop())
    return True



def make_history():
    snap = []
    for player in players_list:
        snap.append(player.copy())

    history.append(snap)