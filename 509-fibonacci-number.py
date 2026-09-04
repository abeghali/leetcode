n = 9

# Beginning of solution

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        else:    
            seq = [0, 1]
            for i in range(n-1):
                seq.append(sum(seq[-2:]))
                i += 1
            return seq[-1]

# End of solution

solution = Solution()
print(solution.fib(n))