from collections import Counter
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

def calculate_similarity_score(col1: list[int], col2: list[int]) -> int:
    counts = Counter(col2)
    return sum(x * counts[x] for x in col1)

col1, col2 = process_stdin()
result = calculate_similarity_score(col1, col2)

print(f"\nThe sum of all similarity scores is: {result}")