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
from helpers import assert_path_sum, run_path_sum
from solution import Solution

# %%
# Example test case
root_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
target_sum = 22
expected = [[5, 4, 11, 2], [5, 8, 4, 5]]

# %%
result = run_path_sum(Solution, root_list, target_sum)
result

# %%
assert_path_sum(result, expected)
