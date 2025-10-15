from collections import defaultdict

class HospitalGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.rooms = {}
    
    def add_room(self, room_id, room_name=None):
        if room_name is None:
            room_name = f"Room {room_id}"
        self.rooms[room_id] = room_name
        if room_id not in self.graph:
            self.graph[room_id] = []
    
    def add_hallway(self, room1, room2):
        self.graph[room1].append(room2)
        self.graph[room2].append(room1)
    
    def dfs_traversal(self, start_room):
        visited = set()
        traversal_order = []
        
        def dfs_helper(current_room):
            visited.add(current_room)
            traversal_order.append(current_room)
            
            for adjacent_room in self.graph[current_room]:
                if adjacent_room not in visited:
                    dfs_helper(adjacent_room)
        
        dfs_helper(start_room)
        return traversal_order
    
    def display_traversal(self, traversal_order):
        print("Robot Cleaning Traversal Order:")
        print("-" * 40)
        for i, room_id in enumerate(traversal_order, 1):
            room_name = self.rooms.get(room_id, f"Room {room_id}")
            print(f"{i}. {room_name} (ID: {room_id})")
        print("-" * 40)
    
    def display_graph(self):
        print("Hospital Layout (Graph Representation):")
        print("-" * 40)
        for room_id in sorted(self.graph.keys()):
            room_name = self.rooms.get(room_id, f"Room {room_id}")
            connections = [self.rooms.get(adj, f"Room {adj}") for adj in self.graph[room_id]]
            print(f"{room_name} (ID: {room_id}) -> {', '.join(connections)}")
        print("-" * 40)

def create_sample_hospital():
    hospital = HospitalGraph()
    
    hospital.add_room(0, "Entrance")
    hospital.add_room(1, "Reception")
    hospital.add_room(2, "Waiting Area")
    hospital.add_room(3, "Examination Room 1")
    hospital.add_room(4, "Examination Room 2")
    hospital.add_room(5, "Storage Room")
    
    hospital.add_hallway(0, 1)
    hospital.add_hallway(1, 2)  
    hospital.add_hallway(1, 3) 
    hospital.add_hallway(2, 4)  
    hospital.add_hallway(3, 4) 
    hospital.add_hallway(4, 5)  
    
    return hospital

def create_alternative_hospital():
    hospital = HospitalGraph()
    
    for i in range(6):
        hospital.add_room(i)
    
    hospital.add_hallway(0, 1)
    hospital.add_hallway(0, 2)
    hospital.add_hallway(1, 3)
    hospital.add_hallway(1, 4)
    hospital.add_hallway(2, 5)
    hospital.add_hallway(3, 4)
    
    return hospital

def main():
    print("HOSPITAL CLEANING ROBOT - DFS TRAVERSAL")
    print("=" * 50)
    
    hospital = create_sample_hospital()
    
    hospital.display_graph()
    
    start_room = 0
    traversal_order = hospital.dfs_traversal(start_room)
    
    print(f"\nStarting from: {hospital.rooms[start_room]}")
    hospital.display_traversal(traversal_order)
    
    all_rooms = set(hospital.rooms.keys())
    visited_rooms = set(traversal_order)
    if all_rooms == visited_rooms:
        print("✓ SUCCESS: All rooms have been visited!")
    else:
        print("✗ WARNING: Some rooms were not visited!")
        unvisited = all_rooms - visited_rooms
        print(f"Unvisited rooms: {unvisited}")
    
    print("\n" + "=" * 50)
    print("ALTERNATIVE HOSPITAL LAYOUT")
    print("=" * 50)
    
    hospital2 = create_alternative_hospital()
    hospital2.display_graph()
    traversal_order2 = hospital2.dfs_traversal(0)
    hospital2.display_traversal(traversal_order2)

if __name__ == "__main__":
    main()
