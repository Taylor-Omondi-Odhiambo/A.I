import heapq, random
import weighted_graph

def dijkstra(graph, start, end):
    visited = set()
    priority_queue = [(0, start, [start])]  # (distance, node, path)

    while priority_queue:
        current_distance, current_node, path = heapq.heappop(priority_queue)

        # Check if this path is shorter than the known shortest path
        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            return path

        for neighbour, weight in graph[current_node].items():
            if neighbour not in visited:
                distance = current_distance + weight
                heapq.heappush(priority_queue, (distance, neighbour, path + [neighbour]))

    return None

graph = { 
    'Arad': {'Zerind':75, 'Sibiu':140, 'Timisoara':118},
    'Zerind': {'Arad':75, 'Oradea':71},
    'Oradea': {'Zerind':71, 'Sibiu':151},
    'Sibiu': {'Arad':140, 'Oradea':151, 'Fagaras':99, 'Rimnicu Vilcea':80},
    'Timisoara': {'Arad':118, 'Lugoj':111},
    'Lugoj': {'Timisoara':111, 'Mehadia':70},
    'Mehadia': {'Lugoj':70, 'Drobeta':75},
    'Drobeta': {'Mehadia':75, 'Craiova':120},
    'Craiova': {'Drobeta':120, 'Rimnicu Vilcea':146, 'Pitesti':138},
    'Rimnicu Vilcea': {'Sibiu':80, 'Craiova':146, 'Pitesti':97},
    'Fagaras': {'Sibiu':99, 'Bucharest':211},
    'Pitesti': {'Rimnicu Vilcea':97, 'Craiova':138, 'Bucharest':101},
    'Bucharest': {'Fagaras':211, 'Pitesti':101},
}

 
print(dijkstra(graph, 'Fagaras', 'Zerind'))




# start_end = random.sample(list(weighted_graph.graph.keys()), 2)
# result_path = dijkstra(weighted_graph.graph, start_end[0], start_end[1])

# if result_path is not None:
#     print(f"Shortest path from {start_end[0]} to {start_end[1]}: {result_path}")
# else:
#     print(f"No path from {start_end[0]} to {start_end[1]}")




