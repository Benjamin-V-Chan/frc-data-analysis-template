from utility_functions.print_formats import seperation_bar
import pandas as pd
import os
import traceback
import matplotlib.pyplot as plt

print(seperation_bar)
print("Script 05: Team Comparison Analysis\n")

# File paths
team_performance_data_path = "outputs/team_data/team_performance_data.json"
advanced_team_performance_data_path = "outputs/team_data/advanced_team_performance_data.json"
team_comparison_analysis_stats_path = "outputs/statistics/team_comparison_analysis_stats.txt"
visualizations_dir = "outputs/visualizations"

try:
    # Check if team performance data file exists
    if not os.path.exists(team_performance_data_path):
        raise FileNotFoundError(f"Team performance data file not found: {team_performance_data_path}")

    # Load the team statistics data
    print(f"[INFO] Loading team performance data from: {team_performance_data_path}")
    with open(team_performance_data_path, "r") as infile:
        team_performance_data = pd.read_json(infile, orient="index")

    # Ensure the DataFrame is not empty
    if team_performance_data.empty:
        raise ValueError(f"Team statistics data is empty. Check the file: {team_performance_data_path}")

    # Add calculated metrics
    print("[INFO] Calculating additional metrics.")

    # INSERT ADDITIONAL METRICS CALCULATIONS HERE

    # Save advanced analysis as JSON
    print(f"[INFO] Saving advanced analysis to: {advanced_team_performance_data_path}")
    os.makedirs(os.path.dirname(advanced_team_performance_data_path), exist_ok=True)
    team_performance_data.to_json(advanced_team_performance_data_path, orient="index", indent=4)

    # Rank teams for each metric
    print("[INFO] Ranking teams for metrics.")
    rankable_metrics = [None, None, None] # INSERT METRICS TO RANK HERE
    rankings = {}
    for metric in rankable_metrics:
        ascending = metric in [None, None] # INSERT ACCENDING METRICS HERE
        team_performance_data[f"{metric}_rank"] = team_performance_data[metric].rank(ascending=ascending)
        rankings[metric] = team_performance_data.sort_values(by=metric, ascending=ascending)

    # Save rankings to the text file
    print(f"[INFO] Saving rankings to: {team_comparison_analysis_stats_path}")
    os.makedirs(os.path.dirname(team_comparison_analysis_stats_path), exist_ok=True)
    with open(team_comparison_analysis_stats_path, 'w') as stats_file:
        stats_file.write("Team Rankings by Custom Metrics\n")
        stats_file.write("=" * 80 + "\n\n")

        for metric, ranked_df in rankings.items():
            stats_file.write(f"Rankings by {metric}:\n")
            stats_file.write(
                ranked_df[[metric, f"{metric}_rank"]].to_string(index=True) + "\n\n"
            )

    # Generate visualizations
    print(f"[INFO] Generating visualizations in: {visualizations_dir}")
    os.makedirs(visualizations_dir, exist_ok=True)
    for metric, ranked_df in rankings.items():
        top_n = 10  # Top 10 teams for visualization
        ranked_df.head(top_n).plot(
            y=metric, kind="bar", title=f"Top {top_n} Teams by {metric.replace('_', ' ').title()}", legend=False
        )
        plt.ylabel(metric.replace("_", " ").title())
        plt.xticks(ticks=range(top_n), labels=ranked_df.head(top_n).index, rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(os.path.join(visualizations_dir, f"top_{top_n}_{metric}.png"))
        plt.close()

    print("\nScript 05: Completed.")

except FileNotFoundError as fnf_error:
    print(f"[ERROR] File not found: {fnf_error}")
except ValueError as value_error:
    print(f"[ERROR] Data validation error: {value_error}")
except PermissionError as perm_error:
    print(f"[ERROR] Permission denied while accessing a file: {perm_error}")
except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {e}")
    print(traceback.format_exc())
if e:
    print("\nScript 05: Failed.")

print(seperation_bar)