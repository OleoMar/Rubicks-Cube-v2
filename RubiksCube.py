from Moves import apply_move_state


class Cube2x2:
    def __init__(self, state=None):
        self.state = state or self.solved_state()

    def solved_state(self):
        return ['W']*4 + ['R']*4 + ['B']*4 + ['Y']*4 + ['O']*4 + ['G']*4

    def is_solved(self):
        return all(self.state[i] == self.state[i // 4 * 4] for i in range(len(self.state)))

    def get_neighbors(self):
        return [(move, self.apply_move(move)) for move in self.get_all_moves()]

    def get_all_moves(self):
        return ['U', "U'", 'R', "R'", 'F', "F'", 'D', "D'", 'L', "L'", 'B', "B'"]


    def apply_move(self, move):
        new_state = apply_move_state(self.state, move)
        return Cube2x2(new_state)
