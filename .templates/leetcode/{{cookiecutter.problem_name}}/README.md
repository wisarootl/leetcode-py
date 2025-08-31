# {{cookiecutter.problem_number}}. {{cookiecutter.problem_title}}

**Difficulty:** {{cookiecutter.difficulty}}
**Topics:** {{cookiecutter.topics}}
**Tags:** {% for _, tags in cookiecutter._tags | dictsort %}{{ tags | join(', ') }}{% endfor %}
{%- if cookiecutter.problem_number %}
**LeetCode:** [Problem {{cookiecutter.problem_number}}](https://leetcode.com/problems/{{cookiecutter.problem_name.replace('_', "-")}}/description/)
{%- endif %}

## Problem Description

{{cookiecutter.problem_description}}

## Examples

{%- for _, examples in cookiecutter._examples | dictsort %}
{%- for example in examples %}

### Example {{ loop.index }}:

```
Input: {{ example.input }}
Output: {{ example.output }}
```

{%- endfor %}
{%- endfor %}

## Constraints

{{cookiecutter.constraints}}
