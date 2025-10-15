from collections import deque

def shortest_warehouse_route(warehouse_grid, start, end):
    """
    Finds the shortest path (minimum moves) from start (S) to the 
    end (E) on a 2D grid, avoiding 'X' obstacles, using BFS.
    """
    rows = len(warehouse_grid)
    cols = len(warehouse_grid[0])
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    queue = deque([(start[0], start[1], [start])])
    visited = {start}

    while queue:
        r, c, path = queue.popleft()

        if (r, c) == end:
            return path, len(path) - 1 

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if (0 <= nr < rows and 
                0 <= nc < cols and 
                neighbor not in visited and 
                warehouse_grid[nr][nc] != 'X'):

                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((nr, nc, new_path))
                
    return None, "No feasible aisle route found."

def display_warehouse_path(grid, start, end, path):
    print("\n--- Visual Path Result ---")
    
    path_set = set(path) if path else set()
    
    for r in range(len(grid)):
        row_output = []
        for c in range(len(grid[0])):
            coord = (r, c)
            
            if coord == start:
                row_output.append(" S ") 
            elif coord == end:
                row_output.append(" E ")
            elif grid[r][c] == 'X':
                row_output.append(" X ")
            elif coord in path_set:
                row_output.append(" # ")
            else:
                row_output.append(" . ")
        print("".join(row_output))
    print("--------------------------")


# --- 3. Execution ---

WAREHOUSE_GRID = [
    ['S', '.', 'X', 'X', 'X', '.'],
    ['X', '.', 'X', '.', '.', '.'],
    ['X', '.', 'X', '.', 'X', 'X'],
    ['X', '.', '.', '.', '.', '.'],
    ['X', 'X', 'X', 'X', 'X', 'E'],
    ['X', '.', '.', '.', '.', '.']
]

START_COORD = (0, 0)
END_COORD = (4, 5)   

shortest_route, moves = shortest_warehouse_route(WAREHOUSE_GRID, START_COORD, END_COORD)

print("🏭 Warehouse Inventory Retrieval Optimization 🏭")
print("-" * 55)
print(f"Start (Loading Dock): {START_COORD}")
print(f"End (Storage Bay E):  {END_COORD}")
print("-" * 55)

if shortest_route:
    path_str = " → ".join(str(coord) for coord in shortest_route)
    print(f"✅ Optimal Route Found in **{moves} steps**.")
    print(f"Coordinate Path: {path_str}")
    
    display_warehouse_path(WAREHOUSE_GRID, START_COORD, END_COORD, shortest_route)
else:
    print(f"❌ Result: {moves}")
