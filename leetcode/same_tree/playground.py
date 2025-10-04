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
from helpers import assert_is_same_tree, run_is_same_tree
from solution import Solution

# %%
# Example test case
p_list: list[int | None] = [1, 2, 3]
q_list: list[int | None] = [1, 2, 3]
expected = True

# %%
result = run_is_same_tree(Solution, p_list, q_list)
result

# %%
assert_is_same_tree(result, expected)
