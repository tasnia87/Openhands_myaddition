def leaderboard(players):
    ranked = sorted(players, key=lambda player: (player['score'], player['name']), reverse=True)
    return [player['name'] for player in ranked]
