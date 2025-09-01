class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r=[]
        def bt(start:int,current:List[int],total:int):
            if total==target:
                r.append(list(current))
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                current.append(candidates[i])
                bt(i,current,total+candidates[i])
                current.pop()
        bt(0,[],0)
        return r