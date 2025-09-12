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
from helpers import assert_max_depth, run_max_depth
from solution import Solution

# %%
# Example test case
root_list = [3, 9, 20, None, None, 15, 7]
expected = 3

# %%
result = run_max_depth(Solution, root_list)
result

# %%
assert_max_depth(result, expected)
