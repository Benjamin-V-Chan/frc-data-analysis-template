from utility_functions.print_formats import seperation_bar
import os
import json
import pandas as pd
import numpy as np

team_based_match_data_path = "data/processed/team_based_match_data.json"
team_performance_data_path = "outputs/team_data/team_performance_data.json"


def convert_to_serializable(obj):
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
    all_team_peformance_data = {}

    for team, data in team_data.items():
        matches = data["matches"]
        df = pd.DataFrame(matches)

        team_performance = {}

        team_performance["number_of_matches"] = len(df)

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

        all_team_peformance_data[team] = team_performance

    return all_team_peformance_data


# Main Script Execution
try:
    with open(team_based_match_data_path, 'r') as infile:
        team_data = json.load(infile)

    if not isinstance(team_data, dict):
        pass

    team_performance_data = calculate_team_peformance_data(team_data)

    # Convert data to serializable format
    team_performance_data_serializable = convert_to_serializable(team_performance_data)

    os.makedirs(os.path.dirname(team_performance_data_path), exist_ok=True)
    with open(team_performance_data_path, 'w') as outfile:
        json.dump(team_performance_data_serializable, outfile, indent=4)


except Exception as e:
    pass