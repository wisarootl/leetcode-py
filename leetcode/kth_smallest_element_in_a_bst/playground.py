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
from helpers import assert_kth_smallest, run_kth_smallest
from solution import Solution

# %%
# Example test case
root_list = [3, 1, 4, None, 2]
k = 1
expected = 1

# %%
result = run_kth_smallest(Solution, root_list, k)
result

# %%
assert_kth_smallest(result, expected)
