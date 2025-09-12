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
from helpers import assert_is_valid_bst, run_is_valid_bst
from solution import Solution

# %%
# Example test case
root_list = [2, 1, 3]
expected = True

# %%
result = run_is_valid_bst(Solution, root_list)
result

# %%
assert_is_valid_bst(result, expected)
