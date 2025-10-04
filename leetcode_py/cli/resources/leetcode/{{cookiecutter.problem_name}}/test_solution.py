{% if cookiecutter.test_imports -%}
{{cookiecutter.test_imports}}


{% endif -%}
{% if cookiecutter.test_content -%}
{{cookiecutter.test_content}}


{% endif -%}
{% if cookiecutter.test_class_name -%}
class Test{{cookiecutter.test_class_name}}:
{% if cookiecutter.test_class_content -%}
    {{cookiecutter.test_class_content}}

{% endif -%}
{% for _, methods in cookiecutter._test_methods | dictsort %}
{% for method in methods %}
{% if method.decorator is defined %}
    {{method.decorator}}
{% endif %}
{% if method.test_decorator is defined %}
{% if method.test_decorator %}
    {{method.test_decorator}}
{% endif %}
{% else %}
    @logged_test
{% endif %}
{% if method.parametrize %}
    @pytest.mark.parametrize("{{method.parametrize}}", [{{method.test_cases.list | join(', ')}}])
{% endif %}
    def {{method.name}}{{method.signature}}:
{{method.body}}

{% endfor %}
{% endfor %}
{% endif -%}
