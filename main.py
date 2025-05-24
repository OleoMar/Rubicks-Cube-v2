from RubiksCube import Cube2x2
from DFS import dfs
from BFS import bfs
from Astar import a_star
import time
import random
from TestSolutuion import test_solution

def scramble_cube(cube, moves_count=5):
    moves = cube.get_all_moves()
    for _ in range(moves_count):
        move = random.choice(moves)
        cube = cube.apply_move(move)
    return cube

if __name__ == "__main__":
    original = scramble_cube(Cube2x2(), moves_count=5)
    print("Состояние после перемешивания:", original.state)

    # DFS
    print("\nРешение с помощью DFS:")
    start = time.time()
    result_dfs = dfs(Cube2x2(original.state[:]))
    print("Решение:", result_dfs)
    print("Время:", time.time() - start)
    test_solution("DFS", original, result_dfs)

    # BFS
    print("\nРешение с помощью BFS:")
    start = time.time()
    result_bfs = bfs(Cube2x2(original.state[:]))
    print("Решение:", result_bfs)
    print("Время:", time.time() - start)
    test_solution("BFS", original, result_bfs)

    # A*
    print("\nРешение с помощью A*:")
    start = time.time()
    result_astar = a_star(Cube2x2(original.state[:]))
    print("Решение:", result_astar)
    print("Время:", time.time() - start)
    test_solution("A*", original, result_astar)