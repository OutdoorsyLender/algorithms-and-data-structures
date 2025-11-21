class NFLRecommender:
    def __init__(self):
        # Hash table implementation for NFL teams
        self.team_data = {
            "arizona": {
                "team": "Arizona Cardinals",
                "stadium": "State Farm Stadium",
                "posts": [
                    "Next Game: Cardinals vs 49ers - Sunday 4PM",
                    "Today's Practice: Team prepares for weekend",
                    "Fan Zone: Tailgate information for Sunday"
                ]
            },
            "texas": {
                "team": "Dallas Cowboys",
                "stadium": "AT&T Stadium",
                "posts": [
                    "Cowboys prepare for division rivalry",
                    "Stadium parking information updated",
                    "Team roster changes for next game"
                ]
            }
        }
    
    def get_team_content(self, location):
        """Get local NFL team content using hash table lookup"""
        # Convert location to lowercase
        location = location.lower()
        
        # Lookup in hash table
        team_info = self.team_data.get(location)
        
        team_info = self.display_team_info(team_info)

    
    def display_team_info(self, team_info):
        """Display formatted team information"""
        print("\n=== Local NFL Team Updates ===")
        print(f"Team: {team_info['team']}")
        print(f"Stadium: {team_info['stadium']}")
        print("\nLatest Team Posts:")
        for post in team_info['posts']:
            print(f"- {post}")
        print("=" * 30)

# Test the recommender
def main():
    print("NFL Local Content Recommender - Module 5 Implementation")
    recommender = NFLRecommender()
    
    # Test Arizona location
    print("\nTesting content for Arizona fan:")
    recommender.get_team_content("arizona")
    
    # Test Texas location
    print("\nTesting content for Texas fan:")
    recommender.get_team_content("texas")


if __name__ == "__main__":
    main()