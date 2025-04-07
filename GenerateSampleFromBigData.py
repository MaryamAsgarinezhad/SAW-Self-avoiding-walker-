import random
from SampleSaver import load_samples


def generate_sample(steps, big_sample, n_sample=None):
    if n_sample is None:
        n_sample = len(big_sample) - 1

    sample = []
    for _ in range(n_sample):
        sample.append(big_sample[random.randint(0, len(big_sample) - 1)][0: steps])

    return sample


if __name__ == '__main__':
    big_data = load_samples(20)
    print(generate_sample(10, big_data))
