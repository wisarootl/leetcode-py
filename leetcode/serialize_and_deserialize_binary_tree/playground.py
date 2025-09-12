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
from helpers import assert_serialize_deserialize, run_serialize_deserialize
from solution import Codec

# %%
# Example test case
root_list = [1, 2, 3, None, None, 4, 5]

# %%
result = run_serialize_deserialize(Codec, root_list)
result

# %%
assert_serialize_deserialize(result, root_list)
