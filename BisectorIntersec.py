from SampleSaver import load_samples
from GenerateSampleFromBigData import generate_sample
from PivotSampler import make_saw_samples, make_base_swa


def estimate_bisector_intersection(steps, n_samples, samples=None):
    result = 0
    if samples is None:
        sample = make_base_swa(steps)
        samples = make_saw_samples(sample, n_samples)

    for sample in samples:
        temp = bisector_intersection(sample)
        result += temp

    return result / len(samples)


def bisector_intersection(swa):
    number = 0
    for i in range(1, len(swa)):
        if abs(swa[i][0]) == abs(swa[i][1]):
            number += 1

    return number


if __name__ == '__main__':
    n = 100000
    episode = 1000
    n_steps = 1000
    samples = generate_sample(50, load_samples(50))
    print("50-step bisector intersections: ", estimate_bisector_intersection(100, n, samples))
    samples = generate_sample(100, load_samples(100))
    print("100-step bisector intersections: ", estimate_bisector_intersection(100, n, samples))
    samples = generate_sample(200, load_samples(200))
    print("200-step bisector intersections: ", estimate_bisector_intersection(100, n, samples))
    samples = generate_sample(1000, load_samples(1000))
    print("1000-step bisector intersections: ", estimate_bisector_intersection(100, n, samples))
