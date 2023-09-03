at', 'Inns','BF']
batting_data = batting_data.drop(columns=not_reqbat)
print(batting_data)
not_reqbowl = ['Mat', 'Inns','Ov']
bowling_data = bowling_data.drop(colum