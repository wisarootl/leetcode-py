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
from helpers import assert_build_tree, run_build_tree
from solution import Solution

# %%
# Example test case
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
expected_list = [3, 9, 20, None, None, 15, 7]

# %%
result = run_build_tree(Solution, preorder, inorder)
result

# %%
assert_build_tree(result, expected_list)
