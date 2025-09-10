class Solution:
    # Time: O(V + E) where V = num_courses, E = prerequisites
    # Space: O(V + E) for adjacency list and recursion stack
    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        UNVISITED, VISITING, VISITED = 0, 1, 2

        graph: list[list[int]] = [[] for _ in range(num_courses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        state = [UNVISITED] * num_courses

        def has_cycle(course: int) -> bool:
            if state[course] == VISITING:  # Currently visiting - cycle detected
                return True
            if state[course] == VISITED:
                return False

            state[course] = VISITING
            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True
            state[course] = VISITED
            return False

        for course in range(num_courses):
            if state[course] == UNVISITED and has_cycle(course):
                return False
        return True
