import graphviz
import pytest

from leetcode_py.data_structures import DictTree


class TestDictTree:

    def setup_method(self):
        self.tree: DictTree[str] = DictTree()

    @pytest.mark.parametrize(
        "root_dict, expected_contains",
        [
            ({}, "Empty"),
            ({"a": {"b": {}}}, ["└── a", "    └── b"]),
            ({"a": {}, "b": {}}, ["├── a", "└── b"]),
            ({"a": {"#": True}, "b": {"value": 42}}, ["├── a", "└── b"]),
            ({"a": {"x": {"#": True}}, "b": {"y": {}}}, ["a", "b"]),
            ({1: {2: {}}, 3: {}}, ["├── 1", "└── 3"]),
        ],
    )
    def test_str_representation(self, root_dict, expected_contains):
        self.tree.root = root_dict
        result = str(self.tree)
        if isinstance(expected_contains, str):
            assert result == expected_contains
        else:
            for expected in expected_contains:
                assert expected in result

    def test_empty_node_rendering(self):
        result = self.tree._render_dict_tree({})
        assert result == ""

    def test_html_without_graphviz(self, monkeypatch):
        # Mock graphviz.Digraph to raise ImportError
        def mock_digraph(*args, **kwargs):
            raise ImportError("No module named 'graphviz'")

        monkeypatch.setattr("leetcode_py.data_structures.dict_tree.graphviz.Digraph", mock_digraph)
        self.tree.root = {"a": {}}
        html = self.tree._repr_html_()
        assert "<pre>" in html
        assert "└── a" in html

    def test_html_with_real_graphviz(self):
        self.tree.root = {"a": {"#": True}, "b": 42}
        html = self.tree._repr_html_()
        # Either SVG rendering works or fallback to text
        if "<svg" in html or "svg" in html.lower():
            # Graphviz worked successfully
            assert True
        elif "<pre>" in html:
            # Fallback was used (graphviz executable not found) - this is expected
            assert "└── a" in html or "├── a" in html
        else:
            pytest.fail("Unexpected HTML output format")

    def test_add_dict_nodes_empty(self):
        dot = graphviz.Digraph()
        self.tree._add_dict_nodes(dot, {}, "test")

    def test_empty_tree_html(self):
        html = self.tree._repr_html_()
        assert "Empty" in html
