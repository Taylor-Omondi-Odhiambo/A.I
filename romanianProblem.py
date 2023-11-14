# Name: Mwangangi Neville Kalunda

# Registration number: P15/142646/2021
# University of Nairobi

# Course code: CSC 317
# Assignment: Do the Romanian problem
# The problem revolves around using a bfs to traverse through cities to get to a various destination  

#dependencies
from queue import Queue

#define the bfs function
def bfs(graph, start, goal):
    explored = set() #set because you cannot explore an area twice
    queue = Queue() 
    queue.put([start]) #the queue is initialized with the first city

    if start == goal:
        return "Start and goal are the same!"

    while not queue.empty():
        path = queue.get() # popping the first item
        node = path[-1]

        if node not in explored:
            neighbors = graph[node] #take the neighbours of a particular node

            for neighbor in neighbors:
                new_path = list(path) 
                new_path.append(neighbor)
                queue.put(new_path)

                if neighbor == goal:
                    return new_path 

            explored.add(node)  #add the nighbour to the traversed list

    return "Goal not reachable from the given start node."

# Define the graph for the Romanian problem
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
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova':['Urziceni','Efo rie'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

# Testing the BFS

# start_city = 'Fagaras'
# goal_city = 'Neamt'
start_city = input("Enter your start city: ")
goal_city = input("Enter your goal city: ")

result = bfs(graph, start_city, goal_city)

if type(result) == list:
    print(f"Shortest path from {start_city} to {goal_city}: {result}")
else:
    print(result)