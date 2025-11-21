# Global dictionaries to store all our data
centers = {}
routes = {}

# Define urgency levels (higher number = more important)
urgency_values = {
    "Critical": 4,
    "High": 3,
    "Medium": 2,
    "Low": 1
}

# Define traffic slowdown factors
traffic_slowdown = {
    "Clear": 1.0,
    "Light": 1.2,
    "Moderate": 1.5,
    "Heavy": 2.0,
    "Severe": 3.0
}

def add_center(id, name, urgency, items):
    centers[id] = {
        "name": name,
        "urgency": urgency,
        "items": items
    }
    routes[id] = []

def add_road(from_id, to_id, miles, traffic):
    # Calculate travel time (miles × traffic factor)
    travel_time = miles * traffic_slowdown[traffic]
    
    # Add the road in both directions
    routes[from_id].append((to_id, travel_time))
    routes[to_id].append((from_id, travel_time))

def find_best_route(start_id, end_id):
    # Keep track of distances
    distances = {}
    for center_id in centers:
        distances[center_id] = float('inf')  # Start with infinity
    distances[start_id] = 0  # Distance to start is 0
    
    # Keep track of visited centers
    visited = []
    
    # Remember how we got to each center
    previous = {}
    
    # Visit all centers
    while len(visited) < len(centers):
        # Find the unvisited center with the smallest distance
        current_id = None
        smallest_distance = float('inf')
        
        for center_id in centers:
            if center_id not in visited and distances[center_id] < smallest_distance:
                current_id = center_id
                smallest_distance = distances[center_id]
        
        # If we can't reach any more centers, stop
        if current_id is None:
            break
        
        # Mark as visited
        visited.append(current_id)
        
        # Look at all neighbors
        for neighbor_id, travel_time in routes[current_id]:
            # Make urgent centers appear closer
            urgency_bonus = urgency_values[centers[neighbor_id]["urgency"]] * 2
            adjusted_time = travel_time - urgency_bonus
            if adjusted_time < 0:  # Don't let it go negative
                adjusted_time = travel_time / urgency_values[centers[neighbor_id]["urgency"]]
            
            # If we found a better path, update
            if distances[current_id] + adjusted_time < distances[neighbor_id]:
                distances[neighbor_id] = distances[current_id] + adjusted_time
                previous[neighbor_id] = current_id
    
    # No path found
    if end_id not in previous and end_id != start_id:
        return [], "No path found"
    
    # Create the path list
    path = []
    current = end_id
    
    # Work backwards from the end
    while current != start_id:
        path.insert(0, current)
        current = previous[current]
    
    # Add the start to the beginning
    path.insert(0, start_id)
    
    return path, distances[end_id]

# Create our test network
def setup_test_network():
    # Add centers
    add_center(1, "Main Hub", "High", ["Water", "Food"])
    add_center(2, "Hospital", "Critical", ["Medical"])
    add_center(3, "School", "Medium", ["Food", "Clothing"])
    add_center(4, "Shelter", "High", ["Blankets", "Water"])
    add_center(5, "Clinic", "Critical", ["Medical", "Water"])
    
    # Add roads
    add_road(1, 2, 10, "Moderate")  # Main Hub to Hospital
    add_road(1, 3, 5, "Light")      # Main Hub to School
    add_road(2, 5, 8, "Heavy")      # Hospital to Clinic
    add_road(3, 4, 6, "Clear")      # School to Shelter
    add_road(3, 5, 12, "Severe")    # School to Clinic
    add_road(4, 5, 7, "Moderate")   # Shelter to Clinic

def print_route_info(start_id, end_id):
    """Print information about a route between two centers"""
    path, distance = find_best_route(start_id, end_id)
    
    start_name = centers[start_id]["name"]
    end_name = centers[end_id]["name"]
    
    print(f"\nBest route from {start_name} to {end_name}:")
    
    if path:
        # Print the path with center names
        route = []
        for id in path:
            route.append(centers[id]["name"])
        
        print(" -> ".join(route))
        print(f"Route priority score: {distance:.1f}")
    else:
        print("No route found!")

def main():
    print("Wildfire Donation Route Finder")
    print("-" * 30)
    
    # Create our test network
    setup_test_network()
    
    # Print the centers
    print("\nOur Donation Centers:")
    for id in centers:
        print(f"{id}. {centers[id]['name']} - {centers[id]['urgency']} priority")
        print(f"   Needs: {', '.join(centers[id]['items'])}")
    
    # Find a route from Main Hub to Hospital 
    print_route_info(1, 2)  # Main Hub to Hospital
    
    # Find a route from Main Hub to Shelter 
    print_route_info(1, 4)  # Main Hub to Shelter
    
    # Find a route from Main Hub to Clinic 
    print_route_info(1, 5)  # Main Hub to Clinic
    
    print("\nProgram completed successfully.")

# Run the program
if __name__ == "__main__":
    main()