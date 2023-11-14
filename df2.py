# Define the graph as an adjacency list
graph = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti']
}

# Define edge weights (distances)
weights = {
    ('Arad', 'Zerind'): 75,
    ('Arad', 'Sibiu'): 140,
    ('Arad', 'Timisoara'): 118,
    ('Zerind', 'Oradea'): 71,
    ('Oradea', 'Sibiu'): 151,
    ('Sibiu', 'Fagaras'): 99,
    ('Sibiu', 'Rimnicu Vilcea'): 80,
    ('Timisoara', 'Lugoj'): 111,
    ('Lugoj', 'Mehadia'): 70,
    ('Mehadia', 'Drobeta'): 75,
    ('Drobeta', 'Craiova'): 120,
    ('Craiova', 'Rimnicu Vilcea'): 146,
    ('Craiova', 'Pitesti'): 138,
    ('Rimnicu Vilcea', 'Pitesti'): 97,
    ('Fagaras', 'Bucharest'): 211,
    ('Pitesti', 'Bucharest'): 101
}

def dfs_with_weights(graph, weights, start, goal, path=None, cost=0):
    if path is None:
        path = [start]

    if start == goal:
        return path, cost

    if start not in graph:
        return None

    shortest_path = None

    for neighbor in graph[start]:
        if neighbor not in path:
            new_result = dfs_with_weights(graph, weights, neighbor, goal, path + [neighbor], cost + weights.get((start, neighbor), 0))

            if new_result is not None:
                new_path, new_cost = new_result
                if shortest_path is None or new_cost < shortest_path[1]:
                    shortest_path = (new_path, new_cost)

    return shortest_path


# start_city = 'Arad'
# goal_city = 'Bucharest'
start_city = input("Enter the start city: ")
goal_city = input("Enter the goal city: ")
result = dfs_with_weights(graph, weights, start_city, goal_city)

if result:
    result_path, total_cost = result
    print(f"Shortest Path from {start_city} to {goal_city}: {result_path}")
    print(f"Total Cost: {total_cost}")
else:
    print(f"No path found from {start_city} to {goal_city}")