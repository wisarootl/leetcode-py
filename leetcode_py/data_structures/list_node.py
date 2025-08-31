class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> "ListNode | None":
        if not arr:
            return None
        head = cls(arr[0])
        current = head
        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return head

    def to_list(self) -> list[int]:
        result = []
        current: "ListNode | None" = self
        while current:
            result.append(current.val)
            current = current.next
        return result

    def __str__(self) -> str:
        return " -> ".join(str(val) for val in self.to_list())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def _repr_html_(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False
        return self.to_list() == other.to_list()
