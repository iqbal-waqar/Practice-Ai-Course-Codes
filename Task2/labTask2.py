BOGGLE_BOARD = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]

INPUT_DICTIONARY = set([
    "START", "NOTE", "SAND", "STONED", "RANT", "RATE", "MEAT", "FATE", "GONE", "LOAN", "LONE"
])

found_words = set()

DIRECTIONS = [
    (-1, 0),  
    (1, 0),  
    (0, 1), 
    (0, -1),
    (-1, 1), 
    (-1, -1),
    (1, 1),  
    (1, -1)  
]



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self, dictionary):
        self.root = TrieNode()
        for word in dictionary:
            self.insert(word.upper()) 

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def solve_boggle(board, dictionary):
    M = len(board)
    N = len(board[0])
    trie = Trie(dictionary)
    
    found_words_set = set()

    def dfs(r, c, current_word, visited):
        if not trie.starts_with(current_word):
            return

        if trie.search(current_word):
            found_words_set.add(current_word)
        
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < M and 0 <= nc < N and (nr, nc) not in visited:
                
                visited.add((nr, nc))
                
                new_char = board[nr][nc]
                dfs(nr, nc, current_word + new_char, visited)
                
                visited.remove((nr, nc))

    for r in range(M):
        for c in range(N):
            start_char = board[r][c]
            dfs(r, c, start_char, set([(r, c)]))

    return sorted(list(found_words_set))



# --- EXECUTION ---

valid_words = solve_boggle(BOGGLE_BOARD, INPUT_DICTIONARY)

print("--- Boggle Solver Results ---")
print(f"Boggle Board Size: {len(BOGGLE_BOARD)}x{len(BOGGLE_BOARD[0])}")
print(f"Input Dictionary: {sorted(list(INPUT_DICTIONARY))}")
print("-" * 35)
print(f"Valid Words Found ({len(valid_words)} total):")

print(valid_words)

example_words = ["NOTE", "SAND", "STONED"]
found_example = all(word in valid_words for word in example_words)
print("-" * 35)
print(f"Verification: Did the solution find the example words {example_words}? {'✅ YES' if found_example else '❌ NO'}")
