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
from helpers import assert_find_median_sorted_arrays, run_find_median_sorted_arrays
from solution import Solution

# %%
# Example test case
nums1 = [1, 3]
nums2 = [2]
expected = 2.0

# %%
result = run_find_median_sorted_arrays(Solution, nums1, nums2)
result

# %%
assert_find_median_sorted_arrays(result, expected)
