MAP_OF_ROMANIA = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcera', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcera': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcera', 146), ('Pitesti', 138)],
    'Pitesti': [('Rimnicu Vilcera', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Neamt': [('Iasi', 87)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Urziceni': [('Vaslui', 142), ('Bucharest', 85), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Urziceni', 85), ('Giurgiu', 90)],
    'Giurgiu': [('Bucharest', 90)]
}

START_CITY = 'Arad'
GOAL_CITY = 'Bucharest'



def dfs_path_finder(graph, start, goal):
    """
    Finds a path from the start city to the goal city using Iterative DFS.

    Args:
        graph (dict): The adjacency list of cities and distances.
        start (str): The starting city.
        goal (str): The goal city.

    Returns:
        list or None: The path as a list of cities if found, or None otherwise.
    """

    stack = [[start]]

    while stack:
        current_path = stack.pop()
        current_node = current_path[-1]

        if current_node == goal:
            return current_path

        for neighbor, _ in graph.get(current_node, []):
            if neighbor not in current_path:
                new_path = current_path + [neighbor]
                stack.append(new_path)

    return None

def calculate_distance(graph, path):
    total_distance = 0
    for i in range(len(path) - 1):
        city_a = path[i]
        city_b = path[i + 1]
        
        distance = next((dist for neighbor, dist in graph[city_a] if neighbor == city_b), 0)
        total_distance += distance
        
    return total_distance



# --- Execution ---

found_path = dfs_path_finder(MAP_OF_ROMANIA, START_CITY, GOAL_CITY)

if found_path:
    distance = calculate_distance(MAP_OF_ROMANIA, found_path)
    
    print("✅ DFS Path Found:")
    print("-" * 30)
    print(f"Start: {START_CITY}")
    print(f"Goal: {GOAL_CITY}")
    print(f"\nPath: {' -> '.join(found_path)}")
    print(f"Total Distance: {distance} km")
    print("-" * 30)
    print("Note: DFS finds *a* path, but not necessarily the shortest one.")
else:
    print(f"❌ No path found from {START_CITY} to {GOAL_CITY}.")
