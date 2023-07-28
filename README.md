# Python Metacritic Scraper + SQL Database Queries
*What correlations can be drawn between top-rated games from Metacritic?*

Follow this link to view the final Metacritic Tableau Dashboards:
https://public.tableau.com/app/profile/shawn.radelat

### What is this?

This is a combination of a python program that I wrote to build a database and a list of SQL queries to show my thought
process of how I manipulated the data.

### What is the goal of the Python Scraper?

My initial goal of finding an already established database to practice my SQL was not very inspiring to me and I had 
always wanted to scrape a website for information. Therefore, I decided to write a script to gather my own data. The
data includes the top 100 rated games of all time from Metacritic's website from 5 different platforms: Playstation 4, 
Playstation 5, Xbox One, Xbox Series X, and PC.

The categories of data that I scraped for each game are as follows: title, developer, platform, release date, 
critic score, number of critics, user score, number of users, player mode, ESRB rating, genre

### What are the CSV files?

Metacritic_Games.csv is the direct result of running Scraper.py. Metacritic_Genres.csv is the direct result of
running Genre_Splitter.csv.

### What is the goal of the SQL Queries?

The point of having a text file with all my SQL queries is really just to "show my work." However, it has proven
useful to have these queries documented for myself to return to at a later time. The ultimate goal with this project
is to present the data that I have manipulated in PowerBI or Tableau.

### Why Genre_Splitter.py?

My scraper compiled all of the data and kept it all categorized. However, I needed to be able to access the multiple genres
in any given row individually. In order to do that, I had to write this script to write a new CSV with the counts of all of
the genres.

### Where can I find the Tableau Dashboard you created?

On my Tableu profile! Prefixed with Metacritic. Click here: https://public.tableau.com/app/profile/shawn.radelat
