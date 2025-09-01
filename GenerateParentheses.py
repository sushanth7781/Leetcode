class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r=[]
        def bt(s,o_c,c_c):
            if len(s)==2*n:
                r.append(s)
                return
            if o_c<n:
                bt(s+"(",o_c+1,c_c)
            if c_c<o_c:
                bt(s+")",o_c,c_c+1)
        bt("",0,0)
        return r