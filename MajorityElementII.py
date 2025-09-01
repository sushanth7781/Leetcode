class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        m=defaultdict(int)
        for i in nums:
            m[i]+=1
        n=n//3
        for key,value in m.items():
            if value>n:
                a.append(key)
        return a