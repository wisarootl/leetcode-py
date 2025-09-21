from typing import Generic, TypeVar

import graphviz

from ._utils import handle_graphviz_fallback

# TODO: Remove TypeVar when minimum Python version is 3.12+ (use class DoublyListNode[T]: syntax)
T = TypeVar("T")


class DoublyListNode(Generic[T]):
    def __init__(
        self, val: T, prev: "DoublyListNode[T] | None" = None, next: "DoublyListNode[T] | None" = None
    ):
        self.val = val
        self.prev = prev
        self.next = next

    @classmethod
    def from_list(cls, arr: list[T]) -> "DoublyListNode[T] | None":
        if not arr:
            return None
        head = cls(arr[0])
        current = head
        for val in arr[1:]:
            new_node = cls(val, prev=current)
            current.next = new_node
            current = new_node
        return head

    def _has_cycle(self) -> bool:
        """Detect cycle using Floyd's algorithm in forward direction."""
        slow = fast = self
        while fast and fast.next and fast.next.next:
            assert slow.next is not None
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def to_list(self, max_length: int = 1000) -> list[T]:
        result: list[T] = []
        current: "DoublyListNode[T] | None" = self
        visited: set[int] = set()

        while current and len(result) < max_length:
            if id(current) in visited:
                break
            visited.add(id(current))
            result.append(current.val)
            current = current.next
        return result

    def __str__(self) -> str:
        if self._has_cycle():
            result: list[str] = []
            current: "DoublyListNode[T] | None" = self
            visited: dict[int, int] = {}
            position = 0

            while current:
                if id(current) in visited:
                    cycle_pos = visited[id(current)]
                    cycle_val = result[cycle_pos]
                    result_str = " <-> ".join(result)
                    return f"{result_str} <-> ... (cycle back to {cycle_val})"

                visited[id(current)] = position
                result.append(str(current.val))
                current = current.next
                position += 1

        values = self.to_list()
        result_str = " <-> ".join(str(val) for val in values)
        if len(values) >= 1000:
            result_str += " <-> ... (long list)"
        return result_str

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def _repr_html_(self) -> str:
        """Generate HTML representation with bidirectional arrows."""
        try:
            dot = graphviz.Digraph(comment="DoublyLinkedList")
            dot.attr(rankdir="LR")
            dot.attr("node", shape="box", style="rounded,filled", fillcolor="lightgreen")
            dot.attr("edge", color="black")

            current: "DoublyListNode[T] | None" = self
            visited: dict[int, int] = {}
            node_id = 0

            while current:
                if id(current) in visited:
                    cycle_target = visited[id(current)]
                    dot.edge(
                        f"node_{node_id - 1}",
                        f"node_{cycle_target}",
                        color="red",
                        style="dashed",
                        label="cycle",
                    )
                    break

                visited[id(current)] = node_id
                dot.node(f"node_{node_id}", str(current.val))

                if current.next and id(current.next) not in visited:
                    # Forward edge
                    dot.edge(f"node_{node_id}", f"node_{node_id + 1}", label="next")
                    # Backward edge
                    dot.edge(f"node_{node_id + 1}", f"node_{node_id}", label="prev", color="blue")

                current = current.next
                node_id += 1

            return dot.pipe(format="svg", encoding="utf-8")
        except (ImportError, AttributeError, graphviz.ExecutableNotFound) as e:
            return handle_graphviz_fallback(e, self.__str__())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DoublyListNode):
            return False

        if self._has_cycle() or other._has_cycle():
            return False

        return self.to_list() == other.to_list()
