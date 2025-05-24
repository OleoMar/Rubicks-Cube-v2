def rotate_face(state, indices, clockwise=True):
    new_state = state[:]
    a, b, c, d = [state[i] for i in indices]

    if clockwise:
        new_state[indices[0]] = state[indices[2]]
        new_state[indices[1]] = state[indices[0]]
        new_state[indices[2]] = state[indices[3]]
        new_state[indices[3]] = state[indices[1]]
        new_state[indices[0]] = c
        new_state[indices[1]] = a
        new_state[indices[2]] = d
        new_state[indices[3]] = b
    else:
        new_state[indices[0]] = state[indices[1]]
        new_state[indices[1]] = state[indices[3]]
        new_state[indices[2]] = state[indices[0]]
        new_state[indices[3]] = state[indices[2]]
        new_state[indices[0]] = b
        new_state[indices[1]] = d
        new_state[indices[2]] = a
        new_state[indices[3]] = c

    return new_state

def apply_move_state(state, move):
    state = state[:]

    if move == "U":
        indices = [0, 1, 2, 3]
        state = rotate_face(state, indices, clockwise=True)
        state[0], state[4], state[8] = state[8], state[0], state[4]
    elif move == "U'":
        indices = [0, 1, 2, 3]
        state = rotate_face(state, indices, clockwise=False)
        state[0], state[4], state[8] = state[4], state[8], state[0]

    elif move == "R":
        indices = [4, 5, 6, 7]
        state = rotate_face(state, indices, clockwise=True)
        state[1], state[5], state[9] = state[9], state[1], state[5]
    elif move == "R'":
        indices = [4, 5, 6, 7]
        state = rotate_face(state, indices, clockwise=False)
        state[1], state[5], state[9] = state[5], state[9], state[1]

    elif move == "F":
        indices = [8, 9, 10, 11]
        state = rotate_face(state, indices, clockwise=True)
        state[2], state[6], state[10] = state[10], state[2], state[6]
    elif move == "F'":
        indices = [8, 9, 10, 11]
        state = rotate_face(state, indices, clockwise=False)
        state[2], state[6], state[10] = state[6], state[10], state[2]
    elif move == "D":
        indices = [12, 13, 14, 15]
        state = rotate_face(state, indices, clockwise=True)
        state[2], state[6], state[10], state[18], state[22], state[14] = \
            state[18], state[22], state[14], state[2], state[6], state[10]

    elif move == "D'":
        indices = [12, 13, 14, 15]
        state = rotate_face(state, indices, clockwise=False)
        state[2], state[6], state[10], state[18], state[22], state[14] = \
            state[10], state[14], state[18], state[2], state[6], state[22]

    elif move == "L":
        indices = [16, 17, 18, 19]
        state = rotate_face(state, indices, clockwise=True)
        state[0], state[8], state[12], state[20] = state[20], state[0], state[8], state[12]

    elif move == "L'":
        indices = [16, 17, 18, 19]
        state = rotate_face(state, indices, clockwise=False)
        state[0], state[8], state[12], state[20] = state[8], state[12], state[20], state[0]

    elif move == "B":
        indices = [20, 21, 22, 23]
        state = rotate_face(state, indices, clockwise=True)
        state[1], state[5], state[13], state[17] = state[17], state[1], state[5], state[13]

    elif move == "B'":
        indices = [20, 21, 22, 23]
        state = rotate_face(state, indices, clockwise=False)
        state[1], state[5], state[13], state[17] = state[5], state[13], state[17], state[1]

    return state