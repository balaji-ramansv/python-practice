# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

class Solution:
    def hamming_distance(self, x: int, y: int) -> int:
        max_elt = max(x,y)
        min_elt = min(x,y)
        max_elt_bin = str(bin(max_elt)).replace("0b", "")
        min_elt_bin = str(bin(min_elt)).replace("0b", "")
        if len(min_elt_bin) < len(max_elt_bin):
            diff = len(max_elt_bin) - len(min_elt_bin)
            diff_pre_pad = "0" * diff
            min_elt_bin = f"{diff_pre_pad}{min_elt_bin}"
        dist = 0
        for i in range(len(min_elt_bin)):
            if min_elt_bin[i] != max_elt_bin[i]:
                dist += 1
        return dist

sol = Solution()
print(sol.hamming_distance(3,1))
