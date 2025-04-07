import numpy as np
import random


def make_saw_samples(base_swa, episodes):
    samples = [base_swa]
    for _ in range(episodes):
        samples.append(transform(samples[len(samples) - 1], random.randint(1, 7)))

    return samples


def transform(swa, transform_id):
    if transform_id < 4:
        return rotation(swa, transform_id)
    else:
        return reflection(swa, transform_id - 3)


def rotation(swa, rotation_id):
    pivot_number = random.randint(0, len(swa) - 1)
    pivot = swa[pivot_number]
    rotated = np.copy(swa[0: pivot_number + 1]).tolist()
    for i in range(pivot_number + 1, len(swa)):
        new_node = rotation_from(pivot, swa[i], rotation_id)
        if new_node in swa[0: pivot_number + 1]:
            return swa
        rotated.append(new_node)

    return rotated


def reflection(swa, reflection_id):
    pivot_number = random.randint(0, len(swa) - 1)
    pivot = swa[pivot_number]
    rotated = np.copy(swa[0: pivot_number + 1]).tolist()
    for i in range(pivot_number + 1, len(swa)):
        new_node = reflection_from(pivot, swa[i], reflection_id)
        if new_node in swa[0: pivot_number + 1]:
            return swa
        rotated.append(new_node)

    return rotated


def rotation_from(pivot, point, rotation_id):
    diff_vector = [point[0] - pivot[0], point[1] - pivot[1]]

    if rotation_id == 1:
        # Perform the 90-degree rotation
        rotated_point = [-diff_vector[1], diff_vector[0]]

    elif rotation_id == 2:
        # Perform the 180-degree rotation
        rotated_point = [-diff_vector[0], -diff_vector[1]]

    else:
        # Perform the 270-degree rotation
        rotated_point = [diff_vector[1], -diff_vector[0]]

    # Translate the rotated point back to the original position
    rotated_point[0] += pivot[0]
    rotated_point[1] += pivot[1]
    return rotated_point


def reflection_from(pivot, point, rotation_id):
    diff_vector = [point[0] - pivot[0], point[1] - pivot[1]]

    if rotation_id == 1:
        # Perform the y-axis reflection
        rotated_point = [-diff_vector[0], diff_vector[1]]

    elif rotation_id == 2:
        # Perform the x-axis reflection
        rotated_point = [diff_vector[0], -diff_vector[1]]

    elif rotation_id == 3:
        # Perform the +diagonal reflection
        rotated_point = [diff_vector[1], diff_vector[0]]

    else:
        # Perform the +diagonal reflection
        rotated_point = [-diff_vector[1], -diff_vector[0]]

    # Translate the rotated point back to the original position
    rotated_point[0] += pivot[0]
    rotated_point[1] += pivot[1]
    return rotated_point


def make_base_swa(n):
    base = []
    for i in range(n):
        base.append([0, i])

    return base


if __name__ == '__main__':
    episode = 1000
    base = make_base_swa(100)
    sample = make_saw_samples(base, episode)
    print("Sample:", sample)
