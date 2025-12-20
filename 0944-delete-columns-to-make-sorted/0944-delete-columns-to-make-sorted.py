class Solution(object):
    def minDeletionSize(self, strs):
        """
        Count columns that are not sorted lexicographically.
        
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        
        # Iterate through each column index
        for i in range(len(strs[0])):
            last = 'a'  # Track the last seen character in this column
            
            # Check characters in this column from top to bottom
            for letters in strs:
                if letters[i] < last:  # Found an unsorted pair!
                    count += 1
                    break  # No need to check rest of this column
                last = letters[i]  # Update last seen character
        
        return count