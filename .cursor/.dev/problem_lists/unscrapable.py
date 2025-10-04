# Unscrapable Problems List
# Problems that cannot be scraped due to being premium, having API issues, or other technical limitations

# Format: (problem_number, problem_name)
UNSCRAPABLE_PROBLEMS = [
    (252, "meeting-rooms"),
    (253, "meeting-rooms-ii"),
    (261, "graph-valid-tree"),
    (271, "encode-and-decode-strings"),
    (323, "number-of-connected-components-in-an-undirected-graph"),
    # Add more unscrapable problems as discovered
]


# Helper function to check if a problem is unscrapable
def is_unscrapable(problem_number: int) -> bool:
    """Check if a problem number is in the unscrapable list."""
    return any(num == problem_number for num, _ in UNSCRAPABLE_PROBLEMS)


def is_unscrapable_by_name(problem_name: str) -> bool:
    """Check if a problem name is in the unscrapable list."""
    return any(name == problem_name for _, name in UNSCRAPABLE_PROBLEMS)


def get_unscrapable_numbers() -> set[int]:
    """Get all unscrapable problem numbers as a set."""
    return {num for num, _ in UNSCRAPABLE_PROBLEMS}
