# donation-route-planner-dijkstra

This project uses Dijkstra’s algorithm to plan donation delivery routes during a wildfire scenario. Each donation center has an urgency level, and each road has distance and traffic conditions.

This project was completed for CSC506 – Module 7.

## How It Works

The program runs in the terminal and does the following:

1. Donation centers are stored with urgency and needed items.
2. Roads between centers include distance and traffic.
3. A modified version of Dijkstra’s algorithm calculates the best routes.
4. Urgency levels affect route priority.
5. The program prints recommended routes and scores.

## Features

**Donation Center Data**
- Name  
- Urgency  
- Needed supplies  

**Road Network**
- Weighted distances  
- Traffic factors  
- Priority scoring  

**Routing Algorithm**
- Modified Dijkstra  
- Path reconstruction  
- Readable route summaries  

## Files Included

**dijkstra_donation_route.py**  
Main script containing the graph data and routing logic.

**dijkstra_donation_route.pdf**  
Write-up explaining the project and what I learned.

## How to Run the Program

```
python dijkstra_donation_route.py
```

## What I Learned

This project helped me understand how pathfinding works and how algorithms like Dijkstra can be adjusted for real-world factors such as urgency and traffic. It also helped me see how graphs are represented in Python.

## Author
Brandon Everett
