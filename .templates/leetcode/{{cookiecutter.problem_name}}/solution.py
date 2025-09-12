{% if cookiecutter.solution_imports -%}
{{cookiecutter.solution_imports}}


{% endif -%}
{% if cookiecutter.solution_contents -%}
{{cookiecutter.solution_contents}}
{% endif -%}
{% if cookiecutter.solution_class_name -%}


class {{cookiecutter.solution_class_name}}:
{% if cookiecutter.solution_class_content -%}
{{cookiecutter.solution_class_content}}

{% endif -%}
{% if cookiecutter._solution_methods -%}
{% for _, methods in cookiecutter._solution_methods | dictsort %}
{% for method in methods %}
    # Time: O(?)
    # Space: O(?)
{% if method.decorator is defined %}    {{method.decorator}}
{% endif %}    def {{method.name}}{{method.signature}}:
{{method.body}}

{% endfor %}
{% endfor %}
{% endif -%}
{% endif -%}
