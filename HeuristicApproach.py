def simple_face_heuristic(cube):
    score = 0
    for i in range(0, len(cube.state), 4):
        face = cube.state[i:i+4]
        if not all(sticker == face[0] for sticker in face):
            score += 1
    return score