import random


N = 5


def conflicts(state):
    count = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                count += 1
    return count

# Generate a random initial state
def random_state():
    return [random.randint(0, N - 1) for _ in range(N)]


def hill_climbing():
    current = random_state()
    current_conflicts = conflicts(current)

    while True:
        neighbors = []

        for col in range(N):
            for row in range(N):
                if row != current[col]:
                    neighbor = current.copy()
                    neighbor[col] = row
                    neighbors.append(neighbor)

        next_state = current
        next_conflicts = current_conflicts

        for state in neighbors:
            c = conflicts(state)
            if c < next_conflicts:
                next_state = state
                next_conflicts = c

        if next_conflicts >= current_conflicts:
            return current

        current = next_state
        current_conflicts = next_conflicts

# Run Hill Climbing
solution = hill_climbing()
print("Solution:", solution)
print("Conflicts:", conflicts(solution))


