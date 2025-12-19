import heapq


N = 5


def is_safe(state, row):
    col = len(state)  # Next column to place
    for c, r in enumerate(state):
        # Check row and diagonal conflicts
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True


def heuristic(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# A* Search function
def a_star_search():
    
    pq = []
    heapq.heappush(pq, (0, 0, []))  # Initial state

    while pq:
        f, g, state = heapq.heappop(pq)

        
        if len(state) == N:
            return state

     
        for row in range(N):
            if is_safe(state, row):
                new_state = state + [row]
                new_g = g + 1
                new_h = heuristic(new_state)
                new_f = new_g + new_h
                heapq.heappush(pq, (new_f, new_g, new_state))

    return None

# Run A*
solution = a_star_search()
print("Solution:", solution)

