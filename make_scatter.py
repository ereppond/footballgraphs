import pandas as pd
import numpy as np
from autoregression.galgraphs import plot_scatter_matrix
import matplotlib.pyplot as plt

def main():
    defence_3_4 = "Green Bay Packers, Oakland Raiders, Los Angeles Rams, Pittsburgh Steelers, Baltimore Ravens, Arizona Cardinals, Indianapolis Colts, Kansas City Chiefs, New York Jets, Washington Redskins, Denver Broncos, Tennessee Titans, Houston Texans, Chicago Bears".split(',')
    defence_4_3 = "Dallas Cowboys, Atlanta Falcons, Minnesota Vikings, Carolina Panthers, Cincinnati Bengals, Jacksonville Jaguars, Oakland Raiders, Detroit Lions, Cleveland Browns, New England Patriots, Tampa Bay Buccaneers, Seattle Seahawks, Buffalo Bills, Philadelphia Eagles, Los Angeles Chargers, Miami Dolphins, New Orleans Saints, San Francisco 49ers, New York Giants".split(',')
    set(defence_3_4).intersection_update(set(defence_4_3))
    set(defence_3_4).intersection(set(defence_4_3))
    isinteam = [(team in defence_4_3) for team in set(defence_3_4)]
    receiving = pd.read_csv('nflscrapR-data/data/game_team_stats/game_receiving_df.csv')
    passing = pd.read_csv('nflscrapR-data/data/game_team_stats/game_passing_df.csv')
    rushing = pd.read_csv('nflscrapR-data/data/game_team_stats/game_rushing_df.csv')
    passing.columns
    play_by_play_2017 = pd.read_csv('nflscrapR-data/data/season_play_by_play/pbp_2017.csv')
    list(play_by_play_2017.columns)
    all_teams = set(play_by_play_2017["DefensiveTeam"].unique())
    three_four_dict = {
        'KC': 'Kansas City Chiefs',
        'NYJ':'New York Jets',
        'WAS': 'Washington Redskins',
        'TEN': 'Tennessee Titans',
        'OAK': 'Oakland Raiders',
        'HOU': 'Houston Texans',
        'ARI': 'Arizona Cardinals',
        'PIT': 'Pittsburgh Steelers',
        'CHI': 'the Chicago Bears',
        'BAL': 'Baltimore Ravens',
        'IND': 'Indianapolis Colts',
        'LA': 'Los Angeles Rams',
        'GB': 'Green Bay Packers',
        'DEN': 'Denver Broncos'
      }
    three_four = list(three_four_dict)
    four_three = list(all_teams-set(three_four)-{np.nan})
    games_three_four = play_by_play_2017[((play_by_play_2017['down'] == 1.0) | (play_by_play_2017['down'] == 2.0) ) & ( play_by_play_2017['DefensiveTeam'].isin(three_four) )]
    games_four_three = play_by_play_2017[((play_by_play_2017['down'] == 1.0) | (play_by_play_2017['down'] == 2.0) ) & ( play_by_play_2017['DefensiveTeam'].isin(four_three) )]
    pd.set_option('display.height', 20)
    pd.set_option('display.max_rows', 65)
    with pd.option_context("display.max_rows", 10, "display.max_columns", 66):
        print(games_four_three.describe() - games_three_four.describe())
    games_four_three.describe() - games_three_four.describe()
    len(play_by_play_2017['DefensiveTeam'].unique())
    # pd.scatter_matrix(games_three_four)
    games_three_four['alignment'] = 'three_four'
    games_four_three['alignment'] = 'four_three'
    df = pd.DataFrame()
    df = df.append(games_four_three).append(games_three_four)
    plt.style.use('ggplot')
    plot_scatter_matrix(df, y_var_name='alignment')
    plot_scatter_matrix(games_three_four)
    plot_scatter_matrix(games_four_three)

    # autoregression.compare_predictions(games_three_four,'down')


if __name__ == "__main__":
    main()
