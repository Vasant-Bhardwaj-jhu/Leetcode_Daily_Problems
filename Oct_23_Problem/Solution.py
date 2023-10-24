# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False
            
#         return math.log(n, 4).is_integer()

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i=0
        a=0
        while a<=n:
            a=4**i
            if a==n:
                return True
            i+=1
        return False
            