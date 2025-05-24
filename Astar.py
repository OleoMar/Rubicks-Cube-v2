import heapq
import itertools
from HeuristicApproach import simple_face_heuristic

counter = itertools.count()

def a_star(start_cube):
    heap = [(simple_face_heuristic(start_cube), 0, next(counter), start_cube, [])]
    visited = set()

    while heap:
        f, g, _, current, path = heapq.heappop(heap)
        if tuple(current.state) in visited:
            continue
        visited.add(tuple(current.state))

        if current.is_solved():
            return path

        for move, neighbor in current.get_neighbors():
            cost = g + 1
            heapq.heappush(heap, (cost + simple_face_heuristic(neighbor), cost, next(counter), neighbor, path + [move]))

    return []
