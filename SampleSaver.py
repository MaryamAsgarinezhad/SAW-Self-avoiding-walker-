from PivotSampler import make_saw_samples, make_base_swa

import json


def save_samples(steps, n_samples, episodes):
    file = open(f"samples/{steps}_steps_samples.txt", "w")
    sample = make_base_swa(steps)
    samples = make_saw_samples(sample, n_samples)
    encode = json.dumps(samples)
    file.write(encode)
    file.close()
    print(f"fie {steps}_steps_samples.txt is ready!")


def load_samples(steps):
    file = open(f"samples/{steps}_steps_samples.txt", "r")
    decode = json.loads(file.read())
    return decode


if __name__ == '__main__':
    n = 1000000
    episode = 1000
    n_steps = 10

    # save_samples(10, n, episode)
    # save_samples(20, n, episode)
    # save_samples(50, n, episode)
    # save_samples(100, n, episode)
    # save_samples(200, n, episode)
    save_samples(500, n, episode)
    # save_samples(1000, n, episode)
    # save_samples(10000, n, episode)


