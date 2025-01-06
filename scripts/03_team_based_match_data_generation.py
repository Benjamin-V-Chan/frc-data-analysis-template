from utility_functions.print_formats import seperation_bar
import os
import json
import traceback

print(seperation_bar)
print("Script 03: Team-based Match Data Restructuring\n")

# File paths
cleaned_match_data_path = "data/processed/cleaned_match_data.json"
team_based_match_data_path = "data/processed/team_based_match_data.json"

# Functions to restructure and calculate statistics


def restructure_to_team_based(cleaned_file_path, team_file_path):
    """
    Restructures cleaned match data into a team-based format with advanced statistics.

    :param cleaned_file_path: Path to the cleaned JSON file.
    :param team_file_path: Path to save the team-based JSON file.
    """
    try:
        # Load cleaned data
        print(f"[INFO] Loading cleaned data from: {cleaned_file_path}")
        with open(cleaned_file_path, 'r') as infile:
            cleaned_data = json.load(infile)

        if not isinstance(cleaned_data, list):
            raise ValueError("Cleaned data must be a list of matches.")

        # Group matches by team
        team_data = {}
        for match in cleaned_data:
            team = match["metadata"]["robotTeam"]
            if team not in team_data:
                team_data[team] = {"matches": []}
            team_data[team]["matches"].append(match)

        # Add advanced statistics
        for team, data in team_data.items():
            for match in data["matches"]:
                # INSERT ADVANCED STATISTICS CALCULATIONS HERE
                pass

        # Save team-based data
        print(f"[INFO] Saving team-based match data to: {team_file_path}")
        with open(team_file_path, 'w') as outfile:
            json.dump(team_data, outfile, indent=4)

    except FileNotFoundError as e:
        print(f"[ERROR] Cleaned data file not found: {e}")
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to decode JSON: {e}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred during restructuring: {e}")
        print(traceback.format_exc())

# Main script execution
try:
    os.makedirs(os.path.dirname(team_based_match_data_path), exist_ok=True)
    restructure_to_team_based(cleaned_match_data_path, team_based_match_data_path)
    print(f"[INFO] Saving team-based match data: {team_based_match_data_path}")
    print("\nScript 03: Completed.")
except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {e}")
    print(traceback.format_exc())
    print("\nScript 03: Failed.")

print(seperation_bar)