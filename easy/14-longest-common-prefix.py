from typing import List

strs = ["flower","flow","flour"]

# Beginning of solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        shortest_string = min(strs, key=len) if strs else ""
        for i in range(len(shortest_string)):
            if all(shortest_string[i] == string[i] for string in strs):
                longest_common_prefix = longest_common_prefix + shortest_string[i]
                i += 1
            else:
                break
        return longest_common_prefix

# End of solution

solution = Solution()
print(solution.longestCommonPrefix(strs))