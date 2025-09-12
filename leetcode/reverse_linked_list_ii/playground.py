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
from helpers import assert_reverse_between, run_reverse_between
from solution import Solution

# %%
# Example test case
head_list = [1, 2, 3, 4, 5]
left, right = 2, 4
expected_list = [1, 4, 3, 2, 5]

# %%
result = run_reverse_between(Solution, head_list, left, right)
result

# %%
assert_reverse_between(result, expected_list)
