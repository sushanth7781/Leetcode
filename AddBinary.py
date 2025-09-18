class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b1=a
        b2=b
        int1=int(b1,2)
        int2=int(b2,2)
        sum_res=int1+int2
        b_s=bin(sum_res)
        b_s_c=b_s[2:]
        return b_s_c