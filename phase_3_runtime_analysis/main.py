import random
import time
import statistics
import csv
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from search_algorithms import (
    recursive_binary_search,
    iterative_binary_search,
    sequential_search
)


data_sizes = [5000, 50000, 100000, 150000, 1000000]
number_of_trials = 10


def check_result(values, target, index):
    # Making sure that the returned index is correct
    if index == -1:
        assert target not in values
    else:
        assert 0 <= index < len(values)
        assert values[index] == target


def main():
    results = []

    for size in data_sizes:
        recursive_times = []
        iterative_times = []
        sequential_times = []

        print("\nTesting list size:", size)

        for trial in range(number_of_trials):
            values = []

            for i in range(size):
                values.append(random.randint(1, 1000000))

            values.sort()

            if random.random() < 0.5:
                target = random.choice(values)
            else:
                target = 1000001

            # Recursive binary search
            start = time.perf_counter()

            index = recursive_binary_search(
                values, target, 0, len(values) - 1
            )

            elapsed = (time.perf_counter() - start) * 1000000
            check_result(values, target, index)
            recursive_times.append(elapsed)

            # Iterative binary search
            start = time.perf_counter()

            index = iterative_binary_search(values, target)

            elapsed = (time.perf_counter() - start) * 1000000
            check_result(values, target, index)
            iterative_times.append(elapsed)

            # Sequential search
            start = time.perf_counter()

            index = sequential_search(values, target)

            elapsed = (time.perf_counter() - start) * 1000000
            check_result(values, target, index)
            sequential_times.append(elapsed)

            print("Trial", trial + 1, "of", number_of_trials, "complete")

        # Calculate the median time for each algorithm
        recursive_median = statistics.median(recursive_times)
        iterative_median = statistics.median(iterative_times)
        sequential_median = statistics.median(sequential_times)

        print("Recursive binary median:", round(recursive_median, 2), "microseconds")
        print("Iterative binary median:", round(iterative_median, 2), "microseconds")
        print("Sequential median:", round(sequential_median, 2), "microseconds")

        results.append([
            size,
            round(recursive_median, 2),
            round(iterative_median, 2),
            round(sequential_median, 2)
        ])

    # Saves the results to a CSV file
    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "data_size",
            "recursive_binary_us",
            "iterative_binary_us",
            "sequential_us"
        ])

        for result in results:
            writer.writerow(result)

    print("\nAll trials completed.")
    print("Results saved to results.csv")


if __name__ == "__main__":
    main()
