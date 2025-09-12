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
from helpers import assert_my_queue, run_my_queue
from solution import MyQueue

# %%
# Example test case
operations = ["MyQueue", "push", "push", "peek", "pop", "empty"]
inputs = [[], [1], [2], [], [], []]
expected = [None, None, None, 1, 1, False]

# %%
result, queue = run_my_queue(MyQueue, operations, inputs)
print(result)
queue

# %%
assert_my_queue(result, expected)
