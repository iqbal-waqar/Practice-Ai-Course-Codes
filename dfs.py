graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def dfs(start):
    stack = [start]       
    visited = []        

    while stack:        
        node = stack.pop() 
        if node not in visited:  
            print(node)       
            visited.append(node)

            for neighbor in reversed(graph[node]): 
                stack.append(neighbor)

dfs("A")