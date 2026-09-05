from typing import List

nums = [0,4,3,0]
target = 0

# Beginning of solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        i = 0
        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums:
                x_indices = [indices for indices, value in enumerate(nums) if value == x]
                if len(x_indices) > 1:
                    x_indices.remove(nums.index(x))
                    output.extend([nums.index(nums[i]), x_indices[0]])
                    break
                elif len(x_indices) == 1 and x_indices[0] == i:
                    continue
                else:
                    output.extend([nums.index(nums[i]), x_indices[0]])
                    break
            i += 1
        return output

# End of solution

solution = Solution()
print(solution.twoSum(nums, target))