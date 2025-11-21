
#Brandon Everett - Linear Search
#Search Algorithm
def search_jerseys(jerseys, search_word):

    found_jerseys = []
    #Search in 'player' and 'team' 
    for jersey in jerseys:
        if (search_word.lower() in jersey['player'].lower() or 
            search_word.lower() in jersey['team'].lower()):
            found_jerseys.append(jersey)
    
    return found_jerseys

# Test Data
nfl_jerseys = [
    {
        'player': 'Kyler Murray',
        'team': 'Arizona Cardinals',
        'number': '1',
        'price': 129.99
    },
    {
        'player': 'Patrick Mahomes',
        'team': 'Kansas City Chiefs',
        'number': '15',
        'price': 139.99
    },
    {
        'player': 'Travis Kelce',
        'team': 'Kansas City Chiefs',
        'number': '87',
        'price': 129.99
    },
    {
        'player': 'Bijan Robinson',
        'team': 'Atlanta Falcons',
        'number': '7',
        'price': 129.99
    }
]

#input and output
jersey_input = input("What Jersey are you Looking for: ")
jersey_wanted = search_jerseys(nfl_jerseys, jersey_input)
print("\nFound these jerseys:")
for jersey in jersey_wanted:
    print(f"{jersey['player']} #{jersey['number']} - ${jersey['price']}")