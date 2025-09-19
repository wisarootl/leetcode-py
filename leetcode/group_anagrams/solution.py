class Solution:

    # Time: O(n * k) - when k > 26 use counting O(k), when k ≤ 26 use sorting O(k log k)
    # Space: O(n * k)
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[str | tuple[int, ...], list[str]] = {}

        for s in strs:
            if len(s) >= 26:
                # Use counting for short strings (better time)
                # Time: O(k) - single pass through string + O(26) for tuple
                # Space: O(26) = O(1) per key
                count = [0] * 26
                for c in s:
                    count[ord(c) - ord("a")] += 1
                key: tuple[int, ...] | str = tuple(count)
            else:
                # Use sorting for long strings (better space)
                # Time: O(k log k) - sorting dominates
                # Space: O(k) per key
                key: tuple[int, ...] | str = "".join(sorted(s))

            groups.setdefault(key, []).append(s)

        return list(groups.values())
