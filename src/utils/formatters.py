from datetime import timedelta

def format_players_fields(player_list):
    if not player_list:
        return ["No Players Online."], ["No Times Available."]

    player_times = []
    player_names = []

    for player in player_list:
        player_times.append(f"⏰ - {str(timedelta(seconds=int(player.duration)))}")
        player_names.append(f"👥 - {player.name}")

    return player_names, player_times