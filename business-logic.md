# Business Logic — Cricklytics

## Business Overview

Cricklytics is a personalized batting performance prediction system that estimates the number of runs a specific batsman is likely to score in a given match scenario. It uses historical ODI/T20 cricket data and machine learning (Decision Tree & Random Forest Regressors) to deliver contextual, player-level predictions based on opposition, balls faced, overs, and match conditions.

## Core Business Transactions

### 1. Data Collection & Integration

**Sources:**
- Kaggle CSVs: `WC_players.csv`, `Ground_Averages.csv`, `ODI_Match_Results.csv`, `ODI_Match_Totals.csv`
- Cricsheets.org: Ball-by-ball ODI YAML data (parsed into `Batsman_Data` and `Bowler_Data`)

**Pipeline (`script.py`):**
1. Load all CSVs (WC players, batsman stats, bowler stats, ground averages, ODI results, ODI totals)
2. Clean data — strip whitespace, drop fully null rows
3. Normalize player name columns across datasets
4. Merge batsman + bowler stats on Player
5. Join with WC players for match context
6. Enrich with ground averages and team averages
7. Fill missing values, drop empty columns
8. Output: `newplayer.csv` — unified dataset for ML

### 2. Exploratory Data Analysis (EDA)

Performed in the Jupyter notebook to uncover patterns:
- Team participation frequency (matches played per team)
- Win/loss records per team
- Top run-scorers identification
- Feature correlation heatmap (balls faced ↔ runs = strongest correlation)
- Regression plot: Runs vs Balls Faced (positive linear relationship)
- Box plots: Runs by opposition team, runs by match format (ODI vs T20)

### 3. Feature Engineering & Preprocessing

**Input features for ML models:**
| Feature | Description |
|---|---|
| Player (encoded) | Batsman identity |
| Opposition (encoded) | Opponent team |
| Balls Faced | Number of deliveries faced |
| Overs | Match overs context |

**Preprocessing steps:**
- Remove incomplete/null records
- Exclude retired-hurt or did-not-bat entries
- Label encode categorical variables (Player, Opposition, Match Format)
- Feature selection based on correlation analysis

### 4. Prediction Models

**Decision Tree Regressor:**
- Recursively splits data on feature thresholds to minimize MSE
- Produces interpretable tree structure
- R² score: 0.993 (99.3% variance explained)

**Random Forest Regressor:**
- Ensemble of multiple decision trees (bootstrap + feature randomness)
- Averages predictions across trees to reduce overfitting
- More robust generalization than single tree

### 5. Prediction Workflow

```
User Input → [Player, Opposition, Balls Faced, Overs]
    ↓
Label Encode Player & Opposition
    ↓
Create Feature Vector [[player_encoded, opposition_encoded, BF, Overs]]
    ↓
Model.predict(features)
    ↓
Output: Predicted Runs (integer)
```

**Example:**
- Input: Rohit Sharma vs West Indies, 78 balls, 32 overs
- Decision Tree Output: 112 runs
- Random Forest Output: 80 runs

## Business Rules

- Player name and opposition must exist in the training dataset
- Balls faced and overs are required numeric inputs
- Matches with incomplete scorecards are excluded from training
- Retired-hurt innings are not considered valid training data
- If no direct historical matchup exists, model uses learned patterns from similar conditions

## Target Users

| User | Use Case |
|---|---|
| Coaches & Captains | Plan batting orders, set target expectations |
| Selectors | Evaluate player form against specific opponents |
| Fantasy Cricket Players | Pick high-performing batsmen for matchups |
| Commentators | Enrich match narratives with data-backed predictions |
| Cricket Fans | Deeper analytical engagement with the sport |

## Limitations

- No consideration of recent form or injury status
- No weather, pitch, or venue-specific features
- Focused only on batting (no bowling/fielding predictions)
- High R² may indicate overfitting on training data
- Requires historical data to exist for the player
