import heapq

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

# Uniform Cost Search function
def uniform_cost_search():
    # Priority Queue: (cost, state)
    pq = []
    heapq.heappush(pq, (0, []))  # Initial state with cost 0

    while pq:
        cost, state = heapq.heappop(pq)

        # Goal test: 5 queens placed safely
        if len(state) == N:
            return state

        # Generate successors
        for row in range(N):
            if is_safe(state, row):
                new_state = state + [row]
                new_cost = cost + 1
                heapq.heappush(pq, (new_cost, new_state))

    return None

# Run UCS
solution = uniform_cost_search()
print("Solution:", solution)
