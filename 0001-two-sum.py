# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

##################################################
#               ✅ This works ✅
##################################################

from typing import List

nums = [0,4,3,0]
target = 0

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        i = 0
        for i in range(len(nums)):
#            if nums[i] <= target:
#            if nums[i] != target:
#                print(str(nums[i]) + " is smaller than or equal to " + str(target))
            x = target - nums[i]
#               x_indices = [i for i, value in enumerate(x) if value == 3]
#               if x in nums and nums.index(x) != i:
            if x in nums:
                x_indices = [indices for indices, value in enumerate(nums) if value == x]
#                   print(x_indices)
#                   x_indices.remove(nums.index(x))
                if len(x_indices) > 1:
                    x_indices.remove(nums.index(x))
#                       output.extend([nums.index(nums[i]), nums.index(x)])
                    output.extend([nums.index(nums[i]), x_indices[0]])
                    break
                elif len(x_indices) == 1 and x_indices[0] == i:
                    continue
                else:
                    output.extend([nums.index(nums[i]), x_indices[0]])
                    break
#            else:
##                print(str(nums[i]) + " is greater than " + str(target))
#                i += 1
            i += 1
#        print(output)
        return output

solution = Solution()
print(solution.twoSum(nums, target))