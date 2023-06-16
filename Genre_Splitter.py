import pandas as pd
import csv

pd.set_option('display.max_rows', 500)  # visual aid
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)

df = pd.read_csv("C:\\Users\\shawn\\OneDrive\\Desktop\\db\\Final_Games.csv")

dct = {}

for index, row in df.iterrows():
    genre_lst = row["genre"].split(",")  # split string to list
    for genre in genre_lst:
        stripped_genre = genre.strip()
        if stripped_genre == "None":  # empty values that came from the site
            continue
        if stripped_genre not in dct:  # appender
            dct[stripped_genre] = 1
        elif stripped_genre in dct:  # counter
            dct[stripped_genre] += 1

with open("Metacritic_Genres.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["genre", "count"])  # headers
    for k, v in dct.items():
        writer.writerow([k, v])
