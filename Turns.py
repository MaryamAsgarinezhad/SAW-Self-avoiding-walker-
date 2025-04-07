from PivotSampler import make_saw_samples, make_base_swa


def estimate_turns(steps, n_samples, samples=None):
    result = 0
    if samples is None:
        sample = make_base_swa(steps)
        samples = make_saw_samples(sample, n_samples + 9999)

    for sample in samples:
        result += turns_number(sample)

    result /= len(samples)
    return result


def turns_number(swa):
    number = 0
    for i in range(1, len(swa) - 1):
        dir1 = [swa[i][0] - swa[i - 1][0], swa[i][0] - swa[i - 1][0]]
        dir2 = [swa[i + 1][0] - swa[i][0], swa[i + 1][0] - swa[i][0]]

        if dir1 != dir2:
            number += 1

    return number


if __name__ == '__main__':
    n = 1000000
    episode = 10000
    n_steps = 20

    print("20-step turns: ", estimate_turns(20, n, episode))
    print("50-step turns: ", estimate_turns(50, n, episode))
    print("100-step turns: ", estimate_turns(100, n, episode))
    print("200-step turns: ", estimate_turns(200, n, episode))

