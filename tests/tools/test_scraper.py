from leetcode_py.tools.scraper import LeetCodeScraper


class TestLeetCodeScraper:
    """Test cases for LeetCodeScraper with real API calls."""

    def setup_method(self):
        """Set up test fixtures."""
        self.scraper = LeetCodeScraper()

    def test_init(self):
        """Test scraper initialization."""
        assert self.scraper.base_url == "https://leetcode.com/graphql"
        assert "Content-Type" in self.scraper.headers

    def test_get_python_code(self):
        """Test Python code extraction."""
        problem_info = {
            "codeSnippets": [
                {"langSlug": "java", "code": "class Solution {}"},
                {"langSlug": "python3", "code": "class Solution:\n    def test(self):"},
                {"langSlug": "cpp", "code": "class Solution {};"},
            ]
        }

        result = self.scraper.get_python_code(problem_info)
        assert result == "class Solution:\n    def test(self):"

    def test_get_python_code_not_found(self):
        """Test Python code extraction when not available."""
        problem_info = {"codeSnippets": [{"langSlug": "java", "code": "class Solution {}"}]}

        result = self.scraper.get_python_code(problem_info)
        assert result is None

    def test_try_common_slugs_known(self):
        """Test common slug fallback for known problem."""
        result = self.scraper._try_common_slugs(1)
        assert result is not None
        assert result["title"] == "Two Sum"
        assert result["difficulty"] == "Easy"

    def test_try_common_slugs_unknown(self):
        """Test common slug fallback for unknown problem."""
        result = self.scraper._try_common_slugs(9999)
        assert result is None

    def test_get_problem_by_slug_success(self):
        """Test successful problem retrieval by slug."""
        result = self.scraper.get_problem_by_slug("two-sum")

        assert result is not None
        assert result["title"] == "Two Sum"
        assert result["difficulty"] == "Easy"
        assert result["questionFrontendId"] == "1"

    def test_get_problem_by_slug_failure(self):
        """Test failed problem retrieval by slug."""
        result = self.scraper.get_problem_by_slug("non-existent-problem-12345")
        assert result is None

    def test_get_problem_by_number_success(self):
        """Test successful problem retrieval by number."""
        result = self.scraper.get_problem_by_number(1)

        assert result is not None
        assert result["title"] == "Two Sum"
        assert result["questionFrontendId"] == "1"

    def test_format_problem_info_real_data(self):
        """Test problem info formatting with real data."""
        # Get real problem data
        problem_info = self.scraper.get_problem_by_slug("two-sum")
        assert problem_info is not None

        # Format it
        result = self.scraper.format_problem_info(problem_info)

        assert result["number"] == "1"
        assert result["title"] == "Two Sum"
        assert result["difficulty"] == "Easy"
        assert "Array" in result["topics"]
        assert "Hash Table" in result["topics"]
        assert result["python_code"] is not None
        assert "class Solution:" in result["python_code"]
        assert len(result["examples"]) > 0
        assert len(result["constraints"]) > 0
