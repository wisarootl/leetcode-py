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
from helpers import assert_lowest_common_ancestor, run_lowest_common_ancestor
from solution import Solution

# %%
# Example test case
root_list = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p_val = 5
q_val = 1
expected_val = 3

# %%
result = run_lowest_common_ancestor(Solution, root_list, p_val, q_val)
result.val

# %%
assert_lowest_common_ancestor(result, expected_val)
