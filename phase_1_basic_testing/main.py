from search_algorithms import (
    recursive_binary_search,
    iterative_binary_search,
    sequential_search,
)


def run_search_tests():
    test_cases = [
        ("Middle element", [3, 5, 8, 12, 14, 18, 21], 12),
        ("Absent target", [3, 5, 8, 12, 14, 18, 21], 9),
        ("First element", [3, 5, 8, 12, 14, 18, 21], 3),
        ("Last element", [3, 5, 8, 12, 14, 18, 21], 21),
        ("Single element present", [7], 7),
        ("Single element absent", [7], 4),
        ("Empty list", [], 5),
        ("Duplicate values", [2, 4, 4, 4, 8], 4),
    ]

    algorithms = [
        (
            "Recursive Binary Search",
            lambda values, target: recursive_binary_search(
                values, target, 0, len(values) - 1
            ),
        ),
        ("Iterative Binary Search", iterative_binary_search),
        ("Sequential Search", sequential_search),
    ]

    all_passed = True

    for test_name, values, target in test_cases:
        values.sort()

        print(f"\nTest: {test_name}")
        print(f"List: {values}")
        print(f"Target: {target}")

        for algorithm_name, search_function in algorithms:
            index = search_function(values, target)

            # Checks if the returned index identifies the target.
            if index == -1:
                passed = target not in values
            else:
                passed = (
                    0 <= index < len(values)
                    and values[index] == target
                )

            all_passed = all_passed and passed

            print(
                f"{algorithm_name}: "
                f"Found = {index != -1}, "
                f"Index = {index}, "
                f"Pass = {passed}"
            )

    print("\n" + "=" * 45)
    print("All tests passed" if all_passed else "Some tests failed")


if __name__ == "__main__":
    run_search_tests()
