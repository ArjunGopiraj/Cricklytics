# Cricklytics — Personalized Batting Performance Prediction

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-Data-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Compute-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Viz-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-Stats-4C72B0)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

## About

Cricklytics is a machine learning system that predicts how many runs a specific batsman will score in a given match scenario. Unlike team-level predictions, it focuses on **individual player performance** using contextual inputs like opposition, balls faced, overs, and match format.

Built using Decision Tree and Random Forest Regressors trained on historical ODI cricket data from Kaggle and Cricsheets.org, the model achieves an R² score of **0.993** (99.3% accuracy).

## Key Features

- **Player-Level Predictions** — Estimate runs for a specific batsman against a specific team
- **Contextual Inputs** — Considers balls faced, overs, opposition, and match format
- **Dual ML Models** — Decision Tree (interpretable) + Random Forest (robust)
- **Comprehensive EDA** — Correlation analysis, distribution plots, top performer identification
- **Multi-Source Data** — Kaggle CSVs + Cricsheets.org ball-by-ball YAML data
- **High Accuracy** — R² = 0.993 on test data

## How It Works

```
User Input: [Player, Opposition, Balls Faced, Overs]
    ↓
Encode categoricals (Label Encoding)
    ↓
Model.predict(feature_vector)
    ↓
Output: Predicted Runs
```

### Example

```
Input:  Rohit Sharma vs West Indies, 78 balls, 32 overs
Decision Tree Output:  112 runs
Random Forest Output:  80 runs
```

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.x |
| ML Models | Decision Tree Regressor, Random Forest Regressor |
| Data Processing | pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| ML Framework | scikit-learn |
| Environment | Jupyter Notebook |

## Project Structure

```
Cricklytics/
├── odis/                               # Raw ball-by-ball YAML data (Cricsheets.org)
├── Cricket Player Prediction.ipynb     # Main notebook (EDA + ML models + predictions)
├── script.py                           # Data integration & preprocessing pipeline
├── newplayer.csv                       # Final unified dataset
├── WC_players.csv                      # World Cup player roster
├── Ground_Averages.csv                 # Venue-specific averages
├── ODI_Match_Results.csv               # Match outcomes
├── ODI_Match_Totals.csv                # Match aggregate scores
└── .gitignore
```

## Data Pipeline

```
Kaggle CSVs + Cricsheets YAML
        ↓
    script.py (Clean, Merge, Integrate)
        ↓
    newplayer.csv (Unified Dataset)
        ↓
    Jupyter Notebook (EDA → Preprocess → Train → Predict)
```

### Data Sources

| Source | Files |
|---|---|
| Kaggle | WC_players.csv, Ground_Averages.csv, ODI_Match_Results.csv, ODI_Match_Totals.csv |
| Cricsheets.org | Ball-by-ball ODI YAML archives (`odis/` folder) |

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook

### Installation

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Run

```bash
jupyter notebook "Cricket Player Prediction.ipynb"
```

Follow the notebook cells to:
1. Load and explore the dataset
2. Visualize patterns (EDA)
3. Train models
4. Make predictions (interactive input)

## Models

| Model | R² Score | Description |
|---|---|---|
| Decision Tree Regressor | 0.993 | Recursive feature splitting, highly interpretable |
| Random Forest Regressor | High | Ensemble of trees, reduces variance and overfitting |

## EDA Highlights

- **Strongest correlation**: Balls Faced ↔ Runs Scored
- **Format impact**: ODI allows higher individual scores vs T20
- **Opposition effect**: Runs vary significantly by opponent strength
- **Top scorers**: Validated against known cricket statistics

## Limitations

- No live form or injury data
- No weather/pitch/venue condition features
- Batting only (no bowling/fielding predictions)
- High R² may indicate some overfitting
- Requires player to exist in historical dataset

## Future Enhancements

- Player Matchup Analyzer (batsman vs specific bowler)
- Live data feeds for real-time predictions
- Player form indicators (last 5 match averages)
- Venue-specific features (pitch type, weather)
- Bowling performance predictions
- Web/mobile application interface

## Team

- Arjun G. Sundar (2024179001 – MCA SS)
- Swathi K (2024179013 – MCA SS)
- Karan K (2024179022 – MCA SS)

Department of Information Science and Technology, CEG, Anna University, Chennai.

## License

This project is licensed under the MIT License.

---

Built with ❤️ for cricket analytics
