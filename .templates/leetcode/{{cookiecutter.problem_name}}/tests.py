{{cookiecutter.test_imports}}


class Test{{cookiecutter.test_class_name}}:
    {%- for _, helper_methods in cookiecutter._test_helper_methods | dictsort %}
    {%- for method in helper_methods %}
    def {{method.name}}(self{% if method.parameters %}, {{method.parameters}}{% endif %}):
        {{method.body | indent(8, first=False)}}

    {%- endfor %}
    {%- endfor %}

    {%- for _, test_methods in cookiecutter._test_methods | dictsort %}
    {%- for method in test_methods %}
    @pytest.mark.parametrize("{{method.parametrize}}", {{method.test_cases}})
    @logged_test
    def {{method.name}}(self, {{method.parametrize_typed if method.parametrize_typed else method.parametrize}}):
        {{method.body | indent(8, first=False)}}

    {%- endfor %}
    {%- endfor %}
