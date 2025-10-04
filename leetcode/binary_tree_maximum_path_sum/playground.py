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
from helpers import assert_max_path_sum, run_max_path_sum
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3]
expected: int = 6

# %%
result = run_max_path_sum(Solution, root_list)
result

# %%
assert_max_path_sum(result, expected)
