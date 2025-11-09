class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans,temp=0,0
        for i in range(len(citations)):
            temp=min(citations[i],temp+1)
            ans=max(ans,temp)
        return ans