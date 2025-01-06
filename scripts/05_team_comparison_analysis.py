from utility_functions.print_formats import seperation_bar
import pandas as pd
import os
import matplotlib.pyplot as plt

print(seperation_bar)
print("Script 05: Team Comparison Analysis\n")

team_performance_data_path = "outputs/team_data/team_performance_data.json"
advanced_team_performance_data_path = "outputs/team_data/advanced_team_performance_data.json"
team_comparison_analysis_stats_path = "outputs/statistics/team_comparison_analysis_stats.txt"
visualizations_dir = "outputs/visualizations"

with open(team_performance_data_path, "r") as infile:
    team_performance_data = pd.read_json(infile, orient="index")

os.makedirs(os.path.dirname(advanced_team_performance_data_path), exist_ok=True)
team_performance_data.to_json(advanced_team_performance_data_path, orient="index", indent=4)

rankable_metrics = [None, None, None]
rankings = {}
for metric in rankable_metrics:
    ascending = metric in [None, None]
    team_performance_data[f"{metric}_rank"] = team_performance_data[metric].rank(ascending=ascending)
    rankings[metric] = team_performance_data.sort_values(by=metric, ascending=ascending)

os.makedirs(os.path.dirname(team_comparison_analysis_stats_path), exist_ok=True)
with open(team_comparison_analysis_stats_path, 'w') as stats_file:
    stats_file.write("Team Rankings by Custom Metrics\n")
    stats_file.write("=" * 80 + "\n\n")

    for metric, ranked_df in rankings.items():
        stats_file.write(f"Rankings by {metric}:\n")
        stats_file.write(
            ranked_df[[metric, f"{metric}_rank"]].to_string(index=True) + "\n\n"
        )

os.makedirs(visualizations_dir, exist_ok=True)
for metric, ranked_df in rankings.items():
    top_n = 10
    ranked_df.head(top_n).plot(
        y=metric, kind="bar", title=f"Top {top_n} Teams by {metric.replace('_', ' ').title()}", legend=False
    )
    plt.ylabel(metric.replace("_", " ").title())
    plt.xticks(ticks=range(top_n), labels=ranked_df.head(top_n).index, rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(visualizations_dir, f"top_{top_n}_{metric}.png"))
    plt.close()