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
from helpers import assert_remove_nth_from_end, run_remove_nth_from_end
from solution import Solution

# %%
# Example test case
head_list: list[int] = [1, 2, 3, 4, 5]
n = 2
expected: list[int] = [1, 2, 3, 5]

# %%
result = run_remove_nth_from_end(Solution, head_list, n)
result

# %%
assert_remove_nth_from_end(result, expected)
