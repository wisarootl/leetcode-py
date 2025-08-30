import pytest
from loguru import logger
from solution import Solution

from leetcode_py.test_utils import logged_test
{{cookiecutter.imports}}

class Test{{cookiecutter.class_name}}:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "{{cookiecutter.param_names}}",
        [
            {%- for _, test_cases in cookiecutter._test_cases | dictsort %}
            {%- for test_case in test_cases %}
            ({% for arg in test_case.args %}{% if arg is string %}"{{ arg }}"{% else %}{{ arg }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}, {{ test_case.expected }}),
            {%- endfor %}
            {%- endfor %}
        ],
    )
    @logged_test
    def test_{{cookiecutter.method_name}}(self, {{cookiecutter.param_names}}):
        logger.info(f"Testing with {{cookiecutter.input_description}}")
        {%- if cookiecutter.test_setup %}
        {{cookiecutter.test_setup}}
        {%- endif %}
        result = self.solution.{{cookiecutter.method_name}}({{cookiecutter.input_params}})
        {%- if cookiecutter.test_logging %}
        {{cookiecutter.test_logging}}
        {%- else %}
        logger.success(f"Got result: {result}")
        {%- endif %}
        {%- if cookiecutter.assertion_code %}
        {{cookiecutter.assertion_code}}
        {%- else %}
        assert result == {{cookiecutter.expected_param}}
        {%- endif %}
