# nfl-hash-table-recommender

This is a simple Python program that uses a hash table to display NFL team updates based on a user's location. It stores a small set of team information and social media–style posts, then prints the matching content after a lookup.

This project was completed as part of my coursework for CSC506.

## How It Works

The program runs in the terminal and does the following:

1. A `NFLRecommender` object is created.
2. A hash table (Python dictionary) stores team names, stadiums, and posts.
3. The user (or test code) enters a location such as "arizona" or "texas."
4. The program looks up the team in the hash table.
5. The team information and posts are displayed.

## Features

**Hash Table System**
- Stores team name
- Stores stadium name
- Stores example social media posts

**NFLRecommender Class**
- Looks up data using a hash table
- Displays formatted team information
- Demonstrates fast dictionary access

## Files Included

**nfl_hash_recommender.py**  
Main Python script containing the data structure and lookup logic.

**nfl_hash_recommender.pdf**  
Write-up explaining the project and what I learned.

## How to Run the Program

1. Install Python 3.
2. Place `nfl_hash_recommender.py` in a folder.
3. Open a terminal in that folder.
4. Run:

```
python nfl_hash_recommender.py
```

## What I Learned

Creating this project helped me understand how hash tables work in real programs. I learned how dictionaries store and retrieve information instantly, and how a simple lookup can power features similar to location‑based content systems.

## Author
Brandon Everett
