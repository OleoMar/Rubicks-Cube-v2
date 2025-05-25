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
    print("State after scramble:", original.state)

    # DFS
    print("\nSolution using DFS:")
    start = time.time()
    result_dfs = dfs(Cube2x2(original.state[:]))
    print("Solution:", result_dfs)
    print("Time:", time.time() - start)
    test_solution("DFS", original, result_dfs)

    # BFS
    print("\nSolution using BFS:")
    start = time.time()
    result_bfs = bfs(Cube2x2(original.state[:]))
    print("Solution:", result_bfs)
    print("time:", time.time() - start)
    test_solution("BFS", original, result_bfs)

    # A*
    print("\nSolution usingA*:")
    start = time.time()
    result_astar = a_star(Cube2x2(original.state[:]))
    print("Solution:", result_astar)
    print("Time:", time.time() - start)
    test_solution("A*", original, result_astar)