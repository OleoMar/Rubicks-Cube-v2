from collections import deque

def bfs(start_cube):
    queue = deque([(start_cube, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if tuple(current.state) in visited:
            continue
        visited.add(tuple(current.state))

        if current.is_solved():
            return path

        for move, neighbor in current.get_neighbors():
            queue.append((neighbor, path + [move]))
    return []
