{{cookiecutter.solution_imports}}

class {{cookiecutter.solution_class_name}}:
    {%- for _, methods in cookiecutter._solution_methods | dictsort %}
    {%- for method in methods %}
    # Time: O(?)
    # Space: O(?)
    def {{method.name}}(self, {{method.parameters}}) -> {{method.return_type}}:
        # TODO: Implement {{method.name}}
        return {{method.dummy_return}}

    {%- endfor %}
    {%- endfor %}
