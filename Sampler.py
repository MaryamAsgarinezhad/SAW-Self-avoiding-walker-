import numpy as np
import random


def is_valid_move(current_pos, proposed_pos, visited_positions_set):
    # Check if the proposed move is valid
    if np.array_equal(proposed_pos, current_pos):
        return False
    if tuple(proposed_pos) in visited_positions_set:
        return False
    return True


def get_valid_moves(current_pos, visited_positions_set):
    result = []
    for dimension in range(0, len(current_pos)):
        for move in [-1, 1]:
            dest = np.copy(current_pos)
            dest[dimension] = dest[dimension] + move
            if is_valid_move(current_pos, dest, visited_positions_set):
                result.append(dest)

    return result


def generate_self_avoiding_random_walk(n):
    current_pos = np.zeros(2)  # Starting position at the origin
    visited_positions = [current_pos]
    visited_positions_set = set(map(tuple, visited_positions))
    i = 0

    while i < n:
        options = get_valid_moves(current_pos, visited_positions_set)
        if len(options) < 1:
            current_pos = np.zeros(2)  # Starting position at the origin
            visited_positions = [current_pos]
            visited_positions_set = set(map(tuple, visited_positions))
            i = 0
            # current_pos = visited_positions[len(visited_positions) - 2]
            # i = i - 1
            continue

        proposed_pos = random.choice(options)  # Select a single random dimension
        current_pos = proposed_pos
        visited_positions.append(current_pos)
        visited_positions_set.add(tuple(current_pos))
        i = i + 1

    return visited_positions


if __name__ == '__main__':
    n_steps = 200
    sample = generate_self_avoiding_random_walk(n_steps)
    print("Sample:", sample)
