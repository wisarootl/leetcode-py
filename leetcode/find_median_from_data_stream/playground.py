# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
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
from helpers import assert_median_finder, run_median_finder
from solution import MedianFinder

# %%
# Example test case
operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
inputs = [[], [1], [2], [], [3], []]
expected = [None, None, None, 1.5, None, 2.0]

# %%
result, mf = run_median_finder(MedianFinder, operations, inputs)
print(result)
mf

# %%
assert_median_finder(result, expected)
