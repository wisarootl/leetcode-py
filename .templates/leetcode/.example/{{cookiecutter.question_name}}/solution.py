{{cookiecutter.imports}}

class Solution:
    # Time: O(?)
    # Space: O(?)
    def {{cookiecutter.method_name}}(self, {{cookiecutter.parameters}}) -> {{cookiecutter.return_type}}:
        # TODO: Implement solution
        {% if cookiecutter.return_type == 'bool' %}return False{% elif cookiecutter.return_type == 'int' %}return 0{% elif cookiecutter.return_type == 'str' %}return ""{% elif cookiecutter.return_type == 'float' %}return 0.0{% elif cookiecutter.return_type.startswith('list[') %}return []{% elif cookiecutter.return_type.startswith('dict[') %}return {}{% elif cookiecutter.return_type.startswith('set[') %}return set(){% elif cookiecutter.return_type.startswith('tuple[') %}return (){% elif cookiecutter.return_type == 'None' %}return None{% else %}return None {% endif %}
