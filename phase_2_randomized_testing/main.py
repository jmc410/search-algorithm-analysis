import random

from search_algorithms import (
    recursive_binary_search,
    iterative_binary_search,
    sequential_search
)


def main():
    all_passed = True

    for test in range(20):
        # Creates a random sorted list of 20 numbers
        values = []

        for i in range(20):
            values.append(random.randint(1, 100))

        values.sort()

        # Alternates between present and absent targets
        if test % 2 == 0:
            target = random.choice(values)
            expected_to_be_present = True
        else:
            target = 101
            expected_to_be_present = False

        print("\nTest number:", test + 1)
        print("Sorted list:", values)
        print("Target:", target)
        print("Expected to be present:", expected_to_be_present)

        # Recursive binary search
        index = recursive_binary_search(
            values, target, 0, len(values) - 1
        )

        if index == -1:
            correct = target not in values
        else:
            correct = (
                0 <= index < len(values)
                and values[index] == target
            )

        if (index != -1) != expected_to_be_present:
            correct = False

        print("Recursive binary search index:", index)
        print("Recursive result acceptable:", correct)

        if not correct:
            all_passed = False

        # Iterative binary search
        index = iterative_binary_search(values, target)

        if index == -1:
            correct = target not in values
        else:
            correct = (
                0 <= index < len(values)
                and values[index] == target
            )

        if (index != -1) != expected_to_be_present:
            correct = False

        print("Iterative binary search index:", index)
        print("Iterative result acceptable:", correct)

        if not correct:
            all_passed = False

        # Sequential search
        index = sequential_search(values, target)

        if index == -1:
            correct = target not in values
        else:
            correct = (
                0 <= index < len(values)
                and values[index] == target
            )

        if (index != -1) != expected_to_be_present:
            correct = False

        print("Sequential search index:", index)
        print("Sequential result acceptable:", correct)

        if not correct:
            all_passed = False

    print("\nRandomized testing complete.")

    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed.")


if __name__ == "__main__":
    main()

