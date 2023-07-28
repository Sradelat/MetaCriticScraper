import pandas as pd
import csv

# VISUAL AID
pd.set_option('display.max_rows', 500) 
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)

# DATA FRAME
df = pd.read_csv("C:\\Users\\shawn\\OneDrive\\Desktop\\db\\Final_Games.csv")

dct = {}

# STRING SPLITTER / APPENDER
for index, row in df.iterrows():
    genre_lst = row["genre"].split(",")  # split string to list
    for genre in genre_lst:
        stripped_genre = genre.strip()  # get rid of whitespace
        if stripped_genre == "None":  # skip empty values that came from the site
            continue
        if stripped_genre not in dct:  # appends string to dict if not already in dict
            dct[stripped_genre] = 1
        elif stripped_genre in dct:  # increases value of string in dict if already in dict
            dct[stripped_genre] += 1

# WRITE TO CSV
with open("Metacritic_Genres.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["genre", "count"])  # headers
    for k, v in dct.items():
        writer.writerow([k, v])
