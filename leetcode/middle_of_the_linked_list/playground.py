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
from helpers import assert_middle_node, run_middle_node
from solution import Solution

from leetcode_py import ListNode

# %%
# Example test case
head_list = [1, 2, 3, 4, 5]
expected_list = [3, 4, 5]

# %%
result = run_middle_node(Solution, head_list)
ListNode[int].to_list(result) if result else []

# %%
assert_middle_node(result, expected_list)
