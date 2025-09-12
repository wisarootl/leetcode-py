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
from helpers import assert_reverse_list, run_reverse_list
from solution import Solution

# %%
# Example test case
head_list = [1, 2, 3, 4, 5]
expected_list = [5, 4, 3, 2, 1]

# %%
result = run_reverse_list(Solution, head_list)
result

# %%
assert_reverse_list(result, expected_list)
