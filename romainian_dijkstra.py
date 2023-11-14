import heapq

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

def dijkstra(graph, weights, start, goal):
    pq = [(0, start)]
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_vertex == goal:
            path = []
            while previous[current_vertex] is not None:
                path.append(current_vertex)
                current_vertex = previous[current_vertex]
            path.append(start)
            return path[::-1], current_distance

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph[current_vertex]:
            weight = weights.get((current_vertex, neighbor), weights.get((neighbor, current_vertex)))
            if weight is None:
                continue
            
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return None

start_city = input("Enter the start city: ")
goal_city = input("Enter the goal city: ")

result = dijkstra(graph, weights, start_city, goal_city)

if result:
    result_path, total_cost = result
    print(f"Shortest Path from {start_city} to {goal_city}: {result_path}")
    print(f"Total Cost: {total_cost}")
else:
    print(f"No path found from {start_city} to {goal_city}")
