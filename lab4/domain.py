


def create_player(name, nationality, points, tourneys) -> dict:

    if name.strip() == "":
        raise ValueError("Name cannot be empty!")
    if nationality.strip() == "":
        raise ValueError("Nationality cannot be empty!")
    if points < 0:
        raise ValueError("ATP ranking points cannot be negative!")
    if tourneys < 0:
        raise ValueError("Numbers of tournaments won cannot be negative!")

    return {
        "name": name,
        "nationality": nationality,
        "ranking_points": points,
        "tournaments_won": tourneys
    }

def get_points(player):
    return player["ranking_points"]

def get_tourneys(player):
    return player["tournaments_won"]

def check_min_max_points(min_points, max_points):
    if min_points < 0:
        raise ValueError("Minimum points cannot be negative!")
    if max_points < 0:
        raise ValueError("Maximum points cannot be negative!")
    if max_points < min_points:
        raise ValueError("Maximum points cannot be less than minimum points!")

def check_div(div):
    if div == 0:
        raise ValueError("Division by zero is not allowed!")