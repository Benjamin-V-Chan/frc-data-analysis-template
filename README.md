# frc-data-analysis-template

Template to use for FRC team data analysis systems.

## How to use

### Code Development
1. **Based off your JSON file data structure

### Steps

1. **Download libraries**
   - Use `pip install -r requirements.txt`

2. **Prepare Raw Data**:
   - Place raw JSON file in `data/raw` and rename to `raw_match_data.json`

3. **Edit scripts to match JSON data structure**
   - Wherever you see comments that require inserted code, insert your custom code there

4. **Run Scripts in Order**:
   - `python scripts/01_clear_outputs.py`
   - `python scripts/02_data_cleaning_and_preprocessing.py`
   - `python scripts/03_team_statistics_and_data_restructuring.py`
   - `python scripts/04_data_analysis_and_statistics_aggregation.py`
   - `python scripts/05_team_comparison_analysis.py`

4. **View Results**:
   - Cleaned Match Data in `data/processed/cleaned_match_data`.
   - Cleaned Team Matches in `data/processed`.
   - Team-based data in `outputs/team_data`.
   - Scouter Error Leaderboard in `outputs/statistics`.
   - Team Comparison Stats in `outputs/statistics`.
   - Advanced Team Comparison Stats in `outputs/team_data`.
   - Team Statistical Analysis in `outputs/team_data`.
   - Visualizations in `outputs/visualizations`.