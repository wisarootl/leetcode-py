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
from helpers import assert_can_finish, run_can_finish
from solution import Solution

# %%
# Example test case
num_courses = 2
prerequisites = [[1, 0]]
expected = True

# %%
result = run_can_finish(Solution, num_courses, prerequisites)
result

# %%
assert_can_finish(result, expected)
