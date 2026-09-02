x = -121

# Beginning of solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        first_index = 0
        i = 0
        f = 1
        is_palindrome = True
        for i in range(int(len(x_list)/2)):
            if x_list[i] == x_list[first_index-f]:
                i += 1
                f += 1
                continue
            else:
                is_palindrome = False
        return is_palindrome

# End of solution

solution = Solution()
print(solution.isPalindrome(x))