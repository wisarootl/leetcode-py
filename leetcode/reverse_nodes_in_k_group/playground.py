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
from helpers import assert_reverse_k_group, run_reverse_k_group
from solution import Solution

# %%
# Example test case
head_vals = [1, 2, 3, 4, 5]
k = 2
expected_vals = [2, 1, 4, 3, 5]

# %%
result = run_reverse_k_group(Solution, head_vals, k)
result

# %%
assert_reverse_k_group(result, expected_vals)
