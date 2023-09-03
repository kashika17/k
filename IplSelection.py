import pandas as pd
import matplotlib.pyplot as plt
batting_data = pd.read_csv("D:\Data sets (l&b)\BATTING STATS - IPL_2017.csv")
bowling_data = pd.read_csv("D:\Data sets (l&b)\BOWLING STATS - IPL_2017.csv")
#1. DATA LOADING AND INSPECTION
print("Understanding the structure...")
print("Batting data-")
print(batting_data.head())
print("Bowling data-")
print(bowling_data.head())
print("Dimensions-")
print("Batting:",batting_data.shape,"Bowling:",bowling_data.shape)
print("Columns available-")
print("Batting data-")
print(batting_data.dtypes)
print("Bowling data-")
print(bowling_data.dtypes)
#2. DATA CLEANING AND PREPARATION
print("Checking for missing values...")
print("Batting data-")
print(batting_data.isnull().sum())
print("Bowling data-")
print(bowling_data.isnull().sum())
print("Cleaning data")
not_reqbat = ['NO','Inns','BF']
batting_data = batting_data.drop(columns=not_reqbat)
print(batting_data)
not_reqbowl = ['Inns','Ov']
bowling_data = bowling_data.drop(columns=not_reqbowl)
print(bowling_data)
print("Converting datatype")
batting_data["HS"] = pd.to_numeric(batting_data["HS"].str.replace(r'\D', ''), errors="coerce")
print(batting_data.dtypes)
#3. PLAYER PERFORMANCE ANALYSIS
print("Batting performance Analysis")
Strike_rate=batting_data['SR']>130
Strike_rate=batting_data[Strike_rate]
performance_mark_bat= (Strike_rate['SR']+batting_data['Avg'])>=160
factor50 = batting_data['50']/batting_data['Mat']
factor100= batting_data['100']/batting_data['Mat']
filter_bat=batting_data[performance_mark_bat & factor50 & factor100].sort_values(by=['50', '100'],ascending=[False, False])
print(filter_bat)
print('Bowling performance Analysis')
Economy=bowling_data['Econ']<=8
Strike_bowl= bowling_data['SR']<=12
filter_bowl=bowling_data[Economy & Strike_bowl]
print(filter_bowl)
print("All Rounders...")
players_bat=batting_data['Player']
players_bowl=bowling_data['Player']
players_bat_set = set(players_bat)
players_bowl_set = set(players_bowl)
all_round = players_bat_set.intersection(players_bowl_set)
all_round_databat = batting_data[batting_data['Player'].isin(list(all_round))]
print(all_round_databat)
all_round_databowl = bowling_data[bowling_data['Player'].isin(list(all_round))]
print("Analysing All rounders")
all_round_databat['A-R Formula']=all_round_databat['Avg']-all_round_databowl['Avg']
all_round_databat.sort_values(by='A-R Formula',ascending=False,inplace=True)
all_round_databat=all_round_databat.head(6)
print(all_round_databat.dropna())
#4. Team 
print("The final players that can be considered to form a team...")
print("Batsman-")
print(filter_bat)
print("Bowlers-")
print(filter_bowl)
print("All Rounders")
print(all_round_databat.dropna())
