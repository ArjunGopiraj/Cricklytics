import pandas as pd
wc_players = pd.read_csv('/mnt/data/WC_players.csv')
batsman_data = pd.read_csv('/mnt/data/Batsman_Data.csv')
bowler_data = pd.read_csv('/mnt/data/Bowler_data.csv')
ground_avg = pd.read_csv('/mnt/data/Ground_Averages.csv')
odi_results = pd.read_csv('/mnt/data/ODI_Match_Results.csv')
odi_totals = pd.read_csv('/mnt/data/ODI_Match_Totals.csv')
def clean_df(df):
    df = df.dropna(how='all')
    df.columns = df.columns.str.strip()
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
    return df
dfs = [wc_players, batsman_data, bowler_data, ground_avg, odi_results, odi_totals]
dfs = [clean_df(df) for df in dfs]
wc_players, batsman_data, bowler_data, ground_avg, odi_results, odi_totals = dfs

print("Batsman columns:", batsman_data.columns.tolist())
print("Bowler columns:", bowler_data.columns.tolist())

batsman_player_col = [col for col in batsman_data.columns if 'name' in col.lower() or 'player' in col.lower()]
bowler_player_col = [col for col in bowler_data.columns if 'name' in col.lower() or 'player' in col.lower()]
wc_player_col = [col for col in wc_players.columns if 'name' in col.lower() or 'player' in col.lower()]
if batsman_player_col and bowler_player_col and wc_player_col:
    batsman_data = batsman_data.rename(columns={batsman_player_col[0]: 'Player'})
    bowler_data = bowler_data.rename(columns={bowler_player_col[0]: 'Player'})
    wc_players = wc_players.rename(columns={wc_player_col[0]: 'Player'})
    player_stats = pd.merge(batsman_data, bowler_data, on='Player', how='outer')
    wc_player_stats = pd.merge(wc_players, player_stats, on='Player', how='inner')
    if 'Ground' in wc_player_stats.columns and 'Ground' in ground_avg.columns:
        wc_player_stats = pd.merge(wc_player_stats, ground_avg, on='Ground', how='left')
    if 'Team' in wc_player_stats.columns and 'Team' in odi_results.columns:
        team_avg = odi_results.groupby('Team').mean(numeric_only=True).reset_index()
        wc_player_stats = pd.merge(wc_player_stats, team_avg, on='Team', how='left', suffixes=('', '_TeamAvg'))
    if 'Match_ID' in wc_player_stats.columns and 'Match_ID' in odi_totals.columns:
        wc_player_stats = pd.merge(wc_player_stats, odi_totals, on='Match_ID', how='left', suffixes=('', '_MatchTotal'))
    wc_player_stats = wc_player_stats.dropna(axis=1, how='all')
    wc_player_stats = wc_player_stats.fillna(0)
    final_path = '/newplayer.csv'
    wc_player_stats.to_csv(final_path, index=False)
    final_path
else:
    raise ValueError("Could not find matching 'Player' or 'Name' column in batsman, bowler, or WC player data.")
