import math
import matplotlib.pyplot as plt
from SampleSaver import load_samples
from GenerateSampleFromBigData import generate_sample
from PivotSampler import make_saw_samples, make_base_swa


def number_of_hits(steps, n_samples, samples=None):
    if samples is None:
        sample = make_base_swa(steps)
        # for _ in range(n_samples):
        #     sample = make_saw_samples(sample, episodes)
        #     dest = sample[len(sample) - 1]
        #     result += math.sqrt(dest[0] * dest[0] + dest[1] * dest[1])
        samples = make_saw_samples(sample, n_samples)

    hits = []
    for _ in range(0, len(samples[0])):
        hits.append(0)

    for sample in samples:
        for j in range(0, len(samples[0])):
            hits[j] += (circle_hit(sample, j + 1))
            if hits[j] == 0:
                break

    for hit in hits:
        hit = hit / len(samples)

    return hits


def draw_plot(hits):
    x_axis = []
    for i in range(1, len(hits) + 1):
        x_axis.append(i)

    plt.bar(x_axis, hits, tick_label=x_axis,
            width=0.8, color=['red', 'green'])
    # naming the x axis
    plt.xlabel('i value')
    # naming the y axis
    plt.ylabel('number of hits')

    # giving a title to my graph
    plt.title('best i')

    # function to show the plot
    plt.show()


def circle_hit(swa, j):
    number = 0
    for i in range(0, len(swa) - 1):
        dit1 = dist(swa[i])
        dit2 = dist(swa[i + 1])
        if not ((dit1 > j and dit2 > j) or (dit1 < j and dit2 < j)):
            number += 1

    return number


def dist(point):
    return math.sqrt(point[0] ** 2 + point[1] ** 2)


if __name__ == '__main__':
    samples = load_samples(50)
    print("sample loaded!")
    samples = generate_sample(50, samples, 100000)
    draw_plot(number_of_hits(50, 0, samples))
