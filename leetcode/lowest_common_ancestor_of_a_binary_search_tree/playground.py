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
root_list = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p_val = 2
q_val = 8
expected_val = 6

# %%
result = run_lowest_common_ancestor(Solution, root_list, p_val, q_val)
result.val if result else None

# %%
assert_lowest_common_ancestor(result, expected_val)
