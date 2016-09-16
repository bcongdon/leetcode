class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_len = 0
        start = 0
        while start < len(words):
            w, l = set(words[start]), len(words[start])
            start += 1
            for w2 in words[start:]:
                for c in w:
                    if c in w2:
                        break
                else:
                    max_len = max(l * len(w2), max_len)
        return max_len

# Explanation
# Loop through words, remove duplicate characters using set().
# Note, the for loop in 13-15 is actually faster than any().
# Note, this solution faster than using dictionaries.

# Runtime - O(n^2)
# Nested loop to check each word with all the words after it.

# Space Complexity - O(1)
# Done in-place.
