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
from helpers import assert_min_stack_operations, run_min_stack_operations
from solution import MinStack

# %%
# Example test case
operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
inputs = [[], [-2], [0], [-3], [], [], [], []]
expected = [None, None, None, None, -3, None, 0, -2]

# %%
result = run_min_stack_operations(MinStack, operations, inputs)
result

# %%
assert_min_stack_operations(result, expected)
