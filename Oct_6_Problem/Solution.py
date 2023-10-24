class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            x,y = divmod(n, 3)

            if y == 0:
                return 3**x
            elif y == 1:
                return 3**(x-1) * 4
            elif y == 2:
                return 3**(x) * 2
        
        return -1