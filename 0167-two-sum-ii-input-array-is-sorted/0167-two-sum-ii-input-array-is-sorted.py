class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j=n-1
        while(i<j):
            sum=numbers[i]+numbers[j]
            if sum==target:
                return [i+1,j+1]
            if sum>target:
                j=j-1
            if sum<target:
                i=i+1
        
        