from collections import deque


N = 5


def is_safe(state, row):
    col = len(state)  # Next column to place
    for c, r in enumerate(state):
        # Check row and diagonal conflicts
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True


def breadth_first_search():
   
    queue = deque()
    queue.append([])  

    while queue:
        state = queue.popleft()

       
        if len(state) == N:
            return state

    
        for row in range(N):
            if is_safe(state, row):
                new_state = state + [row]
                queue.append(new_state)

    return None

# Run BFS
solution = breadth_first_search()
print("Solution:", solution)

