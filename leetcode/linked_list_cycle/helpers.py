from leetcode_py import ListNode


def create_cycle_list(values: list[int], pos: int) -> ListNode[int] | None:
    if not values:
        return None

    nodes = []
    head = ListNode(values[0])
    nodes.append(head)
    current = head

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        nodes.append(current)

    if pos != -1 and pos < len(nodes):
        current.next = nodes[pos]

    return head


def run_has_cycle(solution_class: type, values: list[int], pos: int):
    head = create_cycle_list(values, pos)
    implementation = solution_class()
    return implementation.has_cycle(head)


def assert_has_cycle(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
