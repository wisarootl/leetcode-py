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
from helpers import assert_is_subtree, run_is_subtree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 4, 5, 1, 2]
sub_root_list: list[int | None] = [4, 1, 2]
expected = True

# %%
result = run_is_subtree(Solution, root_list, sub_root_list)
result

# %%
assert_is_subtree(result, expected)
