def dfs(start_cube, max_depth=10):
    visited = set()

    def recursive_dfs(cube, path, depth):
        if cube.is_solved():
            return path
        if depth >= max_depth or cube in visited:
            return None

        visited.add(cube)

        for move, neighbor in cube.get_neighbors():
            result = recursive_dfs(neighbor, path + [move], depth + 1)
            if result:
                return result

        return None

    return recursive_dfs(start_cube, [], 0)