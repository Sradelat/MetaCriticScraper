from bs4 import BeautifulSoup
import requests
import time
import csv
from datetime import datetime, timedelta
import random
import pandas as pd
import regex as re

# TODO Create separate table for genres. That table can be manipulated with pandas to get counts

# ACCESSES HTML CODE
# TooManyRequests error required me to find headers in devtools->network->click top name of waterfall->request headers
headers = {  # infinite redirects to MetaCritic without headers
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

list_URL = [
    "https://www.metacritic.com/browse/games/score/metascore/all/ps5/filtered",
    "https://www.metacritic.com/browse/games/score/metascore/all/pc/filtered",
    "https://www.metacritic.com/browse/games/score/metascore/all/switch/filtered",
    "https://www.metacritic.com/browse/games/score/metascore/all/xbox-series-x/filtered",
    "https://www.metacritic.com/browse/games/score/metascore/all/ps4/filtered",
    "https://www.metacritic.com/browse/games/score/metascore/all/xboxone/filtered"
]
input(f"Press enter to send request for URL list. ({len(list_URL)} requests)")

# Waiting time pool
choices = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3]

# LINK LIST CREATOR
# link_list = ["https://www.metacritic.com/game/xbox-one/inside"]  # for testing comment below loop
link_list = []
for url in list_URL:
    list_page = requests.get(url, headers=headers)
    parser = BeautifulSoup(list_page.text, "html.parser")
    raw_list = parser.find_all("a", attrs="title")  # pull list of all games on top 100 page
    for game in raw_list:  # format links for ease of use later
        link_list.append("https://www.metacritic.com" + game["href"])
    # DELAY
    print("\nLoading link list..\n")  # Please don't block me
    time.sleep(random.choice(choices))

# PARSES HTML FOR FUTURE COLUMNS
debug_mode = False  # In an effect to not make a mistake and get blocked
if debug_mode is True:
    input(f"Press enter to initiate link list loop. ({len(link_list)} requests) **DEBUG MODE ON**")
else:
    input(f"Press enter to initiate link list loop. ({len(link_list)} requests) **DEBUG MODE OFF**")
    input(f"!!WARNING!! DEBUG MODE IS OFF. ARE YOU SURE?")

# CREATE HEADERS
csv_headers = [
    {"title": "",
     "developer": "",
     "platform": "",
     "release_date": "",
     "critic_score": "",
     "number_of_critics": "",
     "user_score": "",
     "number_of_users": "",
     "player_mode": "",
     "esrb_rating": "",
     "genre": ""}
    ]
with open("Metacritic_Games.csv", "w", newline="") as f:  # writes new table headers
    writer = csv.DictWriter(f, fieldnames=csv_headers[0].keys())
    writer.writeheader()

# ITERATE LINKS AND WRITE ROWS
for url in link_list:
    print(f"Index: {link_list.index(url)}")  # bookmark in case of crash - used once to pick up where left off
    value_page = requests.get(url, headers=headers)
    value_parser = BeautifulSoup(value_page.text, "html.parser")
    # COLUMN VARIABLES
    title = value_parser.find("h1").string
    developer = value_parser.find("span", string="Developer:").find_next_sibling().find("a").string
    platform = value_parser.find("span", attrs={"class": "platform"}).find("a").string.strip()

    release = value_parser.find("span", string="Release Date:").find_next_sibling().string  # starts as string
    datetime_release = datetime.strptime(release, "%b %d, %Y")  # Lesson learned - convert to datetime with parse
    if datetime_release + timedelta(days=3) > datetime.today():  # Games with no reviews get skipped
        print(title)
        print("UNRELEASED GAME DETECTED.")
        continue
    formatted_date = datetime_release.strftime("%m/%d/%Y")  # formatted as desired
    # Date format ended up not being compatible with SQLite. WHOOPS

    meta_score = float(value_parser.find(itemprop="ratingValue").string)
    critics = int(value_parser.find("span", string="based on").find_next().find_next("span").string.strip())

    try:
        pre_user_score = value_parser.find("div", attrs={"class": "userscore_wrap feature_userscore"})
        user_score = float(pre_user_score.find("a").find("div").string)
        users = int(pre_user_score.find_all("a")[1].string.split()[0])
    except (ValueError, AttributeError):  # games with no reviews get skipped
        print(title)
        print("NO REVIEWS DETECTED.")
        continue

    try:
        players = value_parser.find("span", string="# of players:").find_next_sibling().string
    except AttributeError:  # accepting null values on player modes
        players = ""
        print("NULL VALUE DETECTED.")

    try:
        esrb = value_parser.find("span", string="Rating:").find_next_sibling().string
    except AttributeError:  # accepting null values on esrb ratings
        esrb = ""
        print("NULL VALUE DETECTED")

    raw_genre = value_parser.find("span", string="Genre(s): ").find_next_siblings()
    genres = ""
    for i in raw_genre:
        if i is raw_genre[-1]:
            genres += f"{i.string}"
        else:
            genres += f"{i.string}, "

    # WRITE CSV
    categories = [
        {
            "title": title,
            "developer": developer,
            "platform": platform,
            "release_date": formatted_date,
            "critic_score": meta_score,
            "number_of_critics": critics,
            "user_score": user_score,
            "number_of_users": users,
            "player_mode": players,
            "esrb_rating": esrb,
            "genre": genres  # comma escape happens automatically - noice
         }
    ]

    with open("Metacritic_Games.csv", "a", newline="") as f:  # writes one row of data each iteration
        writer = csv.DictWriter(f, fieldnames=categories[0].keys())
        writer.writerow(categories[0])

    # DEBUG PRINTS
    print(
        f"Title: {title}\n"
        f"Developer: {developer}\n"
        f"Platform: {platform.strip()}\n"
        f"Metascore: {meta_score} with {critics} Reviews\n"
        f"User score: {user_score} with {users} Ratings\n"
        f"Release Date: {formatted_date}, Raw Date: {release}\n"
        f"Players: {players}\n"
        f"ESRB Rating: {esrb}"
    )
    genre = f"Genre(s): {genres}\n"
    print(genre)

    if debug_mode is True:
        if url == link_list[8]:
            print("**DEBUG STOP**")
            break

    # DELAY
    print("\nWaiting..\n")  # Please don't block me
    time.sleep(random.choice(choices))
