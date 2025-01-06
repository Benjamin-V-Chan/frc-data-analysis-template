## **Features**
1. **Data Cleaning**:
   - Ensures consistency in raw JSON data.
   - Handles missing or extra keys, incorrect data types, and negative values.
   - Generates a Scouter Error Leaderboard to identify inconsistencies in data collection.

2. **Team-Based Data Restructuring**:
   - Transforms match-level data into team-based summaries.
   - Groups matches by teams for advanced analysis.

3. **Advanced Data Analysis**:
   - Calculates custom statistics (e.g., averages, minimums, maximums, standard deviations).
   - Includes pre-configured metrics like team performance consistency.

4. **Visualizations**:
   - Generates bar charts and rankings for key metrics.
   - Saves visualizations in a dedicated folder for easy sharing.

5. **Customizable**:
   - Fully adaptable for different FRC games or data structures.
   - Easy-to-insert custom metrics in Script 05 with minimal setup.

---

## **Directory Structure**
```
.
├── data/
│   ├── raw/                     # Raw scouting data (place your raw JSON file here)
│   ├── processed/               # Processed data files
├── outputs/
│   ├── statistics/              # Statistical results and logs
│   │   ├── scouter_leaderboard.txt
│   │   ├── team_comparison_analysis_stats.txt
│   ├── team_data/               # Team-based data
│   │   ├── team_performance_data.json
│   │   ├── advanced_team_performance_data.json
│   ├── visualizations/          # Generated visualizations (e.g., bar charts)
├── scripts/
│   ├── 01_clear_files.py                  # Clears output and processed folders
│   ├── 02_data_cleaning_and_preprocessing.py   # Cleans raw data and logs errors
│   ├── 03_team_based_match_data_restructuring.py # Converts match-level data to team-based
│   ├── 04_data_analysis_and_statistics_aggregation.py # Calculates team statistics
│   ├── 05_team_comparison_analysis.py     # Adds advanced metrics and visualizations
├── requirements.txt            # List of Python libraries required for the project
└── README.md                   # Project documentation
```

---

## **Setup Instructions**

### **1. Download Libraries**
Install required libraries using the command:
```bash
pip install -r requirements.txt
```

### **2. Prepare Raw Data**
Place your raw JSON file in the `data/raw/` directory and rename it to:
```
raw_match_data.json
```

### **3. Edit Scripts**
- Adjust the **JSON data structure** in scripts to match your team's scouting format.
- Look for comments such as:
  ```
  # INSERT YOUR CUSTOM CODE HERE
  ```
- Add any additional calculations or processing steps needed.

### **4. Run Scripts in Order**
Execute the following scripts sequentially:
```bash
python scripts/01_clear_files.py
python scripts/02_data_cleaning_and_preprocessing.py
python scripts/03_team_based_match_data_restructuring.py
python scripts/04_data_analysis_and_statistics_aggregation.py
python scripts/05_team_comparison_analysis.py
```

### **5. View Results**
After running all scripts, find your processed data and results in the following locations:

- **Cleaned Match Data**: `data/processed/cleaned_match_data.json`
- **Team-Based Match Data**: `data/processed/team_based_match_data.json`
- **Team Statistics Data**: `outputs/team_data/team_performance_data.json`
- **Advanced Team Statistics**: `outputs/team_data/advanced_team_performance_data.json`
- **Scouter Error Leaderboard**: `outputs/statistics/scouter_leaderboard.txt`
- **Team Comparison Stats**: `outputs/statistics/team_comparison_analysis_stats.txt`
- **Visualizations**: `outputs/visualizations/` (e.g., bar charts for top-performing teams)

---

## **Customizing Metrics**

### **Add New Metrics**
To add custom metrics, modify the `05_team_comparison_analysis.py` script:
- Add new metrics to the `CUSTOM_METRICS` dictionary:
  ```python
  CUSTOM_METRICS = {
      "new_metric_name": {
          "description": "Description of the custom metric.",
          "calculation": lambda df: df["some_column"].apply(your_function),
          "ascending": True  # Set to True if lower values are better, False if higher is better
      }
  }
  ```
- Your metric should:
  - Take the `team_performance_data` DataFrame as input.
  - Output a Pandas Series with calculated values.

---

## **Future Enhancements**
1. **Real-Time Integration**:
   - Support for live data ingestion from scouting apps.
2. **Machine Learning**:
   - Predictive models to forecast match outcomes or team rankings.
3. **Interactive Dashboards**:
   - Web-based dashboards for interactive data exploration and analysis.