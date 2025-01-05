import sys


def process_stdin() -> tuple[list[int], list[int]]:
    print("Enter some lines of text (press Ctrl+D or Ctrl+Z then Enter to end):")
    lines = sys.stdin.readlines()
    print("\nYou entered:")
    for line in lines:
        print(line, end="")
    col1 = [int(line.split()[0]) for line in lines]
    col2 = [int(line.split()[1]) for line in lines]
    return col1, col2

def calculate_sum_of_differences(col1: list[int], col2: list[int]) -> int:
    if len(col1) != len(col2):
        raise ValueError("Lists must have the same length")
    sortedCol1, sortedCol2 = [sorted(lst) for lst in [col1, col2]]
    return sum(abs(a - b) for a, b in zip(sortedCol1, sortedCol2))


col1, col2 = process_stdin()
result = calculate_sum_of_differences(col1, col2)

print(f"\nThe sum of all differences is: {result}")
