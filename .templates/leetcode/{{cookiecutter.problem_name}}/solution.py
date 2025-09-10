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
{% if cookiecutter.solution_methods -%}
{% for method in cookiecutter.solution_methods -%}
    # Time: O(?)
    # Space: O(?)
{% if method.decorator -%}
    {{method.decorator}}
{% endif -%}
    def {{method.name}}{{method.signature}}:
        # TODO: Implement {{method.name}}
        {{method.body}}

{% endfor -%}
{% endif -%}
{% endif -%}
