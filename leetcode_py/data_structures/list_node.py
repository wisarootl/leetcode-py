from typing import Generic, TypeVar

import graphviz

from ._utils import handle_graphviz_fallback

# TODO: Remove TypeVar when minimum Python version is 3.12+ (use class ListNode[T]: syntax)
T = TypeVar("T")


class ListNode(Generic[T]):
    def __init__(self, val: T, next: "ListNode[T] | None" = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[T]) -> "ListNode[T] | None":
        if not arr:
            return None
        head = cls(arr[0])
        current = head
        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return head

    def _has_cycle(self) -> bool:
        """Use Floyd's algorithm to detect if list has a cycle."""
        slow = fast = self
        while fast and fast.next and fast.next.next:
            assert slow.next is not None
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # Use identity comparison to avoid recursion
                return True
        return False

    def to_list(self, max_length: int = 1000) -> list[T]:
        result: list[T] = []
        current: "ListNode[T] | None" = self
        visited: set[int] = set()

        while current and len(result) < max_length:
            if id(current) in visited:
                # Cycle detected
                break
            visited.add(id(current))
            result.append(current.val)
            current = current.next
        return result

    def __str__(self) -> str:
        if self._has_cycle():
            # Show cycle with target value
            result: list[str] = []
            current: "ListNode[T] | None" = self
            visited: dict[int, int] = {}
            position = 0

            while current:
                if id(current) in visited:
                    cycle_pos = visited[id(current)]
                    cycle_val = result[cycle_pos]
                    result_str = " -> ".join(result)
                    return f"{result_str} -> ... (cycle back to {cycle_val})"

                visited[id(current)] = position
                result.append(str(current.val))
                current = current.next
                position += 1

        values = self.to_list()
        result_str = " -> ".join(str(val) for val in values)
        if len(values) >= 1000:
            result_str += " -> ... (long list)"
        return result_str

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def _repr_html_(self) -> str:
        """Generate HTML representation using Graphviz for Jupyter notebooks."""
        try:
            dot = graphviz.Digraph(comment="LinkedList")
            dot.attr(rankdir="LR")  # Left to right layout
            dot.attr("node", shape="box", style="rounded,filled", fillcolor="lightblue")
            dot.attr("edge", color="black")

            current: "ListNode[T] | None" = self
            visited: dict[int, int] = {}
            node_id = 0

            # First pass: create all nodes and track positions
            while current:
                if id(current) in visited:
                    # Cycle detected - add edge back to existing node
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

                # Only add edge if next node exists and we haven't seen it (no cycle)
                if current.next and id(current.next) not in visited:
                    dot.edge(f"node_{node_id}", f"node_{node_id + 1}")
                elif current.next and id(current.next) in visited:
                    # Next iteration will detect cycle, don't add regular edge
                    pass

                current = current.next
                node_id += 1

            return dot.pipe(format="svg", encoding="utf-8")
        except (ImportError, AttributeError, graphviz.ExecutableNotFound) as e:
            return handle_graphviz_fallback(e, self.__str__())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False

        # If either has a cycle, we can't do simple comparison
        if self._has_cycle() or other._has_cycle():
            return False  # For simplicity, consider cyclic lists as not equal

        return self.to_list() == other.to_list()
