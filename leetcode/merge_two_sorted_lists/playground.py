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
from helpers import assert_merge_two_lists, run_merge_two_lists
from solution import Solution

from leetcode_py import ListNode

# %%
# Example test case
list1_vals = [1, 2, 4]
list2_vals = [1, 3, 4]
expected_vals = [1, 1, 2, 3, 4, 4]

# %%
result = run_merge_two_lists(Solution, list1_vals, list2_vals)
ListNode[int].to_list(result) if result else []

# %%
assert_merge_two_lists(result, expected_vals)
