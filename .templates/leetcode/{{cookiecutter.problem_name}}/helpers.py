{% if cookiecutter.helpers_imports -%}
{{cookiecutter.helpers_imports}}
{% endif -%}


{% if cookiecutter.helpers_content -%}
{{cookiecutter.helpers_content}}


{% endif -%}

{% if cookiecutter.helpers_run_name -%}
def run_{{cookiecutter.helpers_run_name}}{{cookiecutter.helpers_run_signature}}:
{{cookiecutter.helpers_run_body}}


{% endif -%}
{% if cookiecutter.helpers_assert_name -%}
def assert_{{cookiecutter.helpers_assert_name}}{{cookiecutter.helpers_assert_signature}}:
{{cookiecutter.helpers_assert_body}}
{% endif -%}
