class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for num in range(low,high+1):
            s=str(num)
            if len(s)%2==0:
                n=len(s)//2
                l_s=sum(int(d) for d in s[:n])
                r_s=sum(int(d)for d in s[n:])
                if l_s==r_s:
                    count+=1
        return count

