import requests

def fetch_player_data(sport, league, player_id):
    url = ""
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Example usage
sport = "football"
league = "nfl"
player_id = "13982"  # Example player ID

player_data = fetch_player_data(sport, league, player_id)

if player_data:
    print(f"Player Name: {player_data['fullName']}")
    print(f"Position: {player_data['position']['abbreviation']}")
    print(f"Team: {player_data['team']['name']}")
