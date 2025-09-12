class Solution:

    # Time: O(n)
    # Space: O(n)
    # Monotonic stack approach
    # Stack stores indices of bars in increasing height order
    # When we find a shorter bar, we calculate area using previous bars
    def largest_rectangle_area(self, heights: list[int]) -> int:

        stack: list[int] = []  # Stack of indices
        max_area = 0

        for i, height in enumerate(heights):
            # While current height is less than stack top height
            # Pop from stack and calculate area with popped height as smallest
            while stack and heights[stack[-1]] > height:
                max_area = max(max_area, self.calculate_area(heights, stack, i))

            stack.append(i)

        while stack:
            max_area = max(max_area, self.calculate_area(heights, stack, len(heights)))

        return max_area

    @staticmethod
    def calculate_area(heights: list[int], stack: list[int], right_bound: int) -> int:
        h = heights[stack.pop()]
        w = right_bound if not stack else right_bound - stack[-1] - 1
        return h * w
