class Solution:
    # Time: O(M^2 * N) where M is length of each word, N is total number of words
    # Space: O(M * N) for the visited sets
    def ladder_length(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        if end_word not in word_list:
            return 0

        if begin_word == end_word:
            return 1

        word_set = set(word_list)
        begin_set = {begin_word}
        end_set = {end_word}
        length = 1

        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_set = set()
            for word in begin_set:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1 :]

                        if new_word in end_set:
                            return length + 1

                        if new_word in word_set:
                            next_set.add(new_word)
                            word_set.remove(new_word)

            begin_set = next_set
            length += 1

        return 0
