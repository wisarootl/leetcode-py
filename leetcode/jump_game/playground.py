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
from helpers import assert_can_jump, run_can_jump
from solution import Solution

# %%
# Example test case
nums = [2, 3, 1, 1, 4]
expected = True

# %%
result = run_can_jump(Solution, nums)
result

# %%
assert_can_jump(result, expected)
