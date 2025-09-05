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
        monkeypatch.setattr(
            "builtins.__import__",
            lambda name, *args: (
                exec("raise ImportError") if name == "graphviz" else __import__(name, *args)
            ),
        )
        self.tree.root = {"a": {}}
        html = self.tree._repr_html_()
        assert "<pre>" in html
        assert "└── a" in html

    def test_html_with_real_graphviz(self):
        try:
            self.tree.root = {"a": {"#": True}, "b": 42}
            html = self.tree._repr_html_()
            assert "<svg" in html or "svg" in html.lower()
        except ImportError:
            pytest.skip("graphviz not available")

    def test_add_dict_nodes_empty(self):
        try:
            import graphviz

            dot = graphviz.Digraph()
            self.tree._add_dict_nodes(dot, {}, "test")
        except ImportError:
            pytest.skip("graphviz not available")

    def test_empty_tree_html(self):
        html = self.tree._repr_html_()
        assert "Empty" in html
