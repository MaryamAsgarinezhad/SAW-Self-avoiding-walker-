import math
from SampleSaver import load_samples
from GenerateSampleFromBigData import generate_sample
from PivotSampler import make_saw_samples, make_base_swa


def estimate_distance(steps, n_samples, samples=None):
    result = 0.0
    if samples is None:
        sample = make_base_swa(steps)
        # for _ in range(n_samples):
        #     sample = make_saw_samples(sample, episodes)
        #     dest = sample[len(sample) - 1]
        #     result += math.sqrt(dest[0] * dest[0] + dest[1] * dest[1])
        samples = make_saw_samples(sample, n_samples)

    for sample in samples:
        dest = sample[len(sample) - 1]
        result += math.sqrt(dest[0] * dest[0] + dest[1] * dest[1])

    result /= len(samples)
    return result


def estimate_v(base_n, n_samples):
    samples1 = load_samples(base_n)
    print("sample loaded!")
    samples1 = generate_sample(base_n, samples1)

    samples2 = load_samples(base_n * 2)
    print("sample loaded!")
    samples2 = generate_sample(base_n * 2, samples2)
    result_1 = estimate_distance(base_n, n_samples, samples1)
    result_2 = estimate_distance(2 * base_n, n_samples, samples2)

    result = result_2/result_1
    v = math.log2(result)
    return v


if __name__ == '__main__':
    n = 1000000
    episode = 1000
    n_steps = 50
    print("Estimated v = ", estimate_v(n_steps, n))
