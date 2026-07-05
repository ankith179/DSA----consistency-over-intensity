class Solution:
    def prime(self,n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def nonSpecialCount(self, l:int , r: int) -> int:
        c = 0
        limit  = math.sqrt(r)
        for i in range(2, int(limit+1)):
            if self.prime(i):
                special = i**2
                if special >= l and special <= r:
                    c += 1
                    
        total = r-l+1
        return total - c