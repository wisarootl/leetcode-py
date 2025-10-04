# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_erase_overlap_intervals, run_erase_overlap_intervals
from solution import Solution

# %%
# Example test case
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
expected = 1

# %%
result = run_erase_overlap_intervals(Solution, intervals)
result

# %%
assert_erase_overlap_intervals(result, expected)
