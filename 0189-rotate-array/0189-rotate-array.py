class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        if k!=n:
            nums.reverse()
            i=0
            j=k-1
            while(j<n and i<j):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            i=k
            j=n-1
            while(j<n and i<j):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1