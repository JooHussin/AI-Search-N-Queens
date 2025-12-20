import heapq


N = 5


def is_safe(state, row):
    col = len(state)  # Next column to place
    for c, r in enumerate(state):
        # Check row and diagonal conflicts
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True


def uniform_cost_search():
 
    pq = []
    heapq.heappush(pq, (0, []))  

    while pq:
        cost, state = heapq.heappop(pq)

       
        if len(state) == N:
            return state

    
        for row in range(N):
            if is_safe(state, row):
                new_state = state + [row]
                new_cost = cost + 1
                heapq.heappush(pq, (new_cost, new_state))

    return None

# Run UCS
solution = uniform_cost_search()
print("Solution:", solution)

