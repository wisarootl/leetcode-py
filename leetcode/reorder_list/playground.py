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
from helpers import assert_reorder_list, run_reorder_list
from solution import Solution

# %%
# Example test case
head_list: list[int] = [1, 2, 3, 4]
expected: list[int] = [1, 4, 2, 3]

# %%
result = run_reorder_list(Solution, head_list)
result

# %%
assert_reorder_list(result, expected)
