from typing import Any, Generic, Hashable, TypeAlias, TypeVar

import graphviz

from ._utils import handle_graphviz_fallback

K = TypeVar("K", bound=Hashable)
RecursiveDict: TypeAlias = dict[K, "RecursiveDict[K] | Any"]


class DictTree(Generic[K]):

    def __init__(self) -> None:
        self.root: RecursiveDict[K] = {}

    def __str__(self) -> str:
        if not hasattr(self, "root") or not self.root:
            return "Empty"
        return self._render_dict_tree(self.root)

    def _render_dict_tree(self, node: RecursiveDict[K], prefix: str = "", depth: int = 0) -> str:
        if not node:
            return ""

        lines = []
        items = list(node.items())

        for i, (key, child) in enumerate(items):
            is_last = i == len(items) - 1
            current_prefix = "└── " if is_last else "├── "
            lines.append(f"{prefix}{current_prefix}{key}")

            if isinstance(child, dict) and child:
                next_prefix = prefix + ("    " if is_last else "│   ")
                child_lines = self._render_dict_tree(child, next_prefix, depth + 1)
                if child_lines:
                    lines.append(child_lines)

        return "\n".join(lines)

    def _repr_html_(self) -> str:
        if not hasattr(self, "root") or not self.root:
            return "<pre>Empty</pre>"

        try:
            dot = graphviz.Digraph()
            dot.attr(rankdir="TB")
            dot.attr("node", shape="box", style="rounded,filled", fillcolor="lightblue")

            self._add_dict_nodes(dot, self.root, "root")
            return dot.pipe(format="svg", encoding="utf-8")
        except (ImportError, AttributeError, graphviz.ExecutableNotFound) as e:
            return handle_graphviz_fallback(e, self.__str__())

    def _add_dict_nodes(
        self, dot: Any, node: RecursiveDict[K], node_id: str, char: K | str = ""
    ) -> None:
        if not node:
            return

        label = char if char else "root"
        dot.node(node_id, label)

        child_count = 0
        for key, child in node.items():
            if isinstance(child, dict):
                child_node_id = f"{node_id}_{child_count}"
                dot.edge(node_id, child_node_id)
                self._add_dict_nodes(dot, child, child_node_id, key)
                child_count += 1
            else:
                leaf_id = f"{node_id}_leaf_{child_count}"
                dot.node(leaf_id, f"{key}: {child}", fillcolor="lightgreen")
                dot.edge(node_id, leaf_id)
                child_count += 1
