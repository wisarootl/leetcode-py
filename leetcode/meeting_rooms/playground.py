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
from helpers import assert_can_attend_meetings, run_can_attend_meetings
from solution import Solution

# %%
# Example test case
intervals = [[0, 30], [5, 10], [15, 20]]
expected = False

# %%
result = run_can_attend_meetings(Solution, intervals)
result

# %%
assert_can_attend_meetings(result, expected)
