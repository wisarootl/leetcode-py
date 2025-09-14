# {{cookiecutter.problem_title}}

**Difficulty:** {{cookiecutter.difficulty}}
**Topics:** {{cookiecutter.topics}}
**Tags:** {% for _, tags in cookiecutter._tags | dictsort %}{{ tags | join(', ') }}{% endfor %}
{% if cookiecutter.problem_number %}
**LeetCode:** [Problem {{cookiecutter.problem_number}}](https://leetcode.com/problems/{{cookiecutter.problem_name.replace('_', "-")}}/description/)
{% endif %}

## Problem Description

{{cookiecutter.readme_description}}

## Examples

{%- for _, examples in cookiecutter._readme_examples | dictsort %}
{%- for example in examples %}

### Example {{loop.index}}:

{{example.content}}
{%- endfor %}
{%- endfor %}

## Constraints

{{cookiecutter.readme_constraints}}

{% if cookiecutter.readme_additional %}
{{cookiecutter.readme_additional}}
{% endif %}
