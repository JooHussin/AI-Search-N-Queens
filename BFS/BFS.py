from collections import deque

# Board size
N = 5

# Function to check if a queen can be safely placed in the given row
def is_safe(state, row):
    col = len(state)  # Next column to place
    for c, r in enumerate(state):
        # Check row and diagonal conflicts
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

# Breadth-First Search function
def breadth_first_search():
    # Queue to store states
    queue = deque()
    queue.append([])  # Initial state (no queens)

    while queue:
        state = queue.popleft()

        # Goal test: 5 queens placed safely
        if len(state) == N:
            return state

        # Generate successors
        for row in range(N):
            if is_safe(state, row):
                new_state = state + [row]
                queue.append(new_state)

    return None

# Run BFS
solution = breadth_first_search()
print("Solution:", solution)
