import pytest
from loguru import logger
from .solution import Solution


class Test{ClassName}:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "{param_names}",
        [
            ({test_case_1}),
            ({test_case_2}),
            ({test_case_3}),
        ],
    )
    def test_{method_name}(self, {param_names}):
        logger.info(f"Testing with {input_description}")
        result = self.solution.{method_name}({input_params})
        logger.success(f"Got result: {result}")
        assert result == {expected_param}
        logger.debug("Test passed! ✨")
