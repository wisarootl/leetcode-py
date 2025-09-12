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
from helpers import assert_has_cycle, create_cycle_list, run_has_cycle
from solution import Solution

# %%
# Example test case
values = [3, 2, 0, -4]
pos = 1
expected = True

# %%
head = create_cycle_list(values, pos)
head

# %%
result = run_has_cycle(Solution, values, pos)
result

# %%
assert_has_cycle(result, expected)
