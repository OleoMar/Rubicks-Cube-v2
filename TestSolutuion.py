from RubiksCube import Cube2x2

def validate_solution(start_state, moves):
    cube = Cube2x2(start_state[:])  # копия начального состояния
    for move in moves:
        cube = cube.apply_move(move)
    return cube.is_solved()

def test_solution(name, start_cube, moves):
    is_valid = validate_solution(start_cube.state, moves)
    print(f"\nCheck the Solution {name}:")
    print("Moves:", moves)
    print("Is Solved:" , " Yes" if is_valid else " No")
