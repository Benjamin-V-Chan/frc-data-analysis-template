from utility_functions.print_formats import seperation_bar
import os
import json
import traceback
import pandas as pd
import numpy as np

print(seperation_bar)
print("Script 04: Data Analysis & Statistics Aggregation\n")

# File paths
team_based_match_data_path = "data/processed/team_based_match_data.json"
team_performance_data_path = "outputs/team_data/team_performance_data.json"

# Helper Functions


def convert_to_serializable(obj):
    """
    Converts all non-serializable types (like NumPy types) to Python native types.

    :param obj: Object to convert.
    :return: Serializable object.
    """
    if isinstance(obj, (pd.Series, pd.DataFrame)):
        return obj.to_dict()
    if isinstance(obj, (np.int64, np.float64)):
        return obj.item()
    if isinstance(obj, (pd.Timestamp, pd.Timedelta)):
        return str(obj)
    if isinstance(obj, (int, float, str, bool, list, dict)):
        return obj
    if hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes)):
        return [convert_to_serializable(item) for item in obj]
    return obj


def calculate_team_peformance_data(team_data):
    """
    Automatically calculates team performance data for each team based on detected data types.

    :param team_data: Dictionary containing match data for each team.
    :return: A dictionary with aggregated team statistics.
    """
    all_team_peformance_data = {}

    for team, data in team_data.items():
        matches = data["matches"]
        df = pd.DataFrame(matches)

        # Initialize team_performance dictionary for this team
        team_performance = {}

        # Number of matches played
        team_performance["number_of_matches"] = len(df)

        # Process data based on detected types
        for column in df.columns:
            if pd.api.types.is_numeric_dtype(df[column]):
                team_performance[f"{column}_average"] = float(df[column].mean())
                team_performance[f"{column}_min"] = float(df[column].min())
                team_performance[f"{column}_max"] = float(df[column].max())
                team_performance[f"{column}_std_dev"] = float(df[column].std())
            elif pd.api.types.is_categorical_dtype(df[column]) or pd.api.types.is_object_dtype(df[column]):
                team_performance[f"{column}_value_counts"] = df[column].value_counts().to_dict()
            elif pd.api.types.is_bool_dtype(df[column]):
                team_performance[f"{column}_percent_true"] = float(df[column].mean() * 100)

        # Add processed statistics for the team
        all_team_peformance_data[team] = team_performance

    return all_team_peformance_data


# Main Script Execution
try:
    print(f"[INFO] Loading team-based match data from: {team_based_match_data_path}")
    with open(team_based_match_data_path, 'r') as infile:
        team_data = json.load(infile)

    if not isinstance(team_data, dict):
        raise ValueError("Team-based match data must be a dictionary.")

    print("[INFO] Calculating team peformance data.")
    team_performance_data = calculate_team_peformance_data(team_data)

    # Convert data to serializable format
    team_performance_data_serializable = convert_to_serializable(team_performance_data)

    print(f"[INFO] Saving team performance data to: {team_performance_data_path}")
    os.makedirs(os.path.dirname(team_performance_data_path), exist_ok=True)
    with open(team_performance_data_path, 'w') as outfile:
        json.dump(team_performance_data_serializable, outfile, indent=4)

    print("\nScript 04: Completed.")

except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {e}")
    print(traceback.format_exc())
    print("\nScript 04: Failed.")

print(seperation_bar)