# REPORT FUNCTIONS
def country_number(players_list):
    country_count = {}
    for player in players_list:
        country = player["nationality"]
        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country] = 1

    print("Number of players from each country:")
    for country, count in country_count.items():
        print(f"{country}: {count}")


def country_won(players_list, country):
    count = sum(player["tournaments_won"] for player in players_list if player["nationality"] == country)
    print(f"Number of tournaments won by players from {country}: {count}")

def substring_search(players_list, substring):
    filtered_players = [player for player in players_list if substring in player["name"]]
    sorted_players = sorted(filtered_players, key=lambda x: x["ranking_points"], reverse=True)
    for player in sorted_players:
        print(f"{player['name']}, {player['nationality']}, {player['ranking_points']}, {player['tournaments_won']}")

def podium(players_list):
    sorted_players = sorted(players_list, key=lambda x: (-x["ranking_points"], -x["tournaments_won"]))
    print("Top 3 players based on ATP ranking points and tournaments won:")
    for player in sorted_players[:3]:
        print(f"{player['name']}, {player['tournaments_won']}")