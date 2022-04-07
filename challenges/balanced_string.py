# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it in the maximum amount of balanced strings.
# Return the maximum amount of split balanced strings.

# Example 1:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

# Example 3:
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".


from concurrent.futures import process


class Solution:
    def balanced_string_split(self, s: str) -> int:
        processed = ""
        balanced_strings = []
        changed = 0
        print(s)
        for c in s:
            processed += c
            if len(processed) < 2:
                continue
            if processed[-1] != processed[-2]:
                changed += 1
            if changed == 2:
                temp_str = processed[0:len(processed)-1]
                min_repeat = min([temp_str.count("L"), temp_str.count("R")]) * 2
                balanced_strings.append(processed[0:min_repeat])
                processed = processed[min_repeat:]
                print(f"temp_str: {temp_str}; min_repeat: {min_repeat}; processed: {processed}")
                if len(processed) == 1:
                    changed = 0
                else:
                    changed = 1
        if processed.count("L") == processed.count("R"):
            balanced_strings.append(processed)
        print(balanced_strings)
        return len(balanced_strings)

print(Solution().balanced_string_split("LLLLRRRR"))

