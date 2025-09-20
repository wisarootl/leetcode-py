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
from helpers import assert_swap_pairs, run_swap_pairs
from solution import Solution

# %%
# Example test case
head_list = [1, 2, 3, 4]
expected = [2, 1, 4, 3]

# %%
result = run_swap_pairs(Solution, head_list)
result

# %%
assert_swap_pairs(result, expected)
