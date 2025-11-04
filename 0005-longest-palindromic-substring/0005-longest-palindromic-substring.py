class Solution:
    def manacher_odd(self, s):
        radii = [0] * len(s)
        c = 0
        r = 0
        
        for center in range(len(s)):
            if center < r:
                mirror = c * 2 - center
                radii[center] = min(r - center, radii[mirror])
            
            while (center + radii[center] + 1 < len(s) and 
                   center - radii[center] - 1 >= 0 and 
                   s[center + radii[center] + 1] == 
                   s[center - radii[center] - 1]):
                radii[center] += 1
            
            if center + radii[center] > r:
                r = center + radii[center]
                c = center
        
        return radii

    def longestPalindrome(self, s):
        preprocessed = '#'.join(s) + '#'
        
        palindrome_radii = self.manacher_odd(preprocessed)
        
        max_radius = max(palindrome_radii)
        max_idx = palindrome_radii.index(max_radius)
        
        start = max_idx - max_radius
        end = max_idx + max_radius + 1
        longest_palindromic_substring = ''.join(
            char for char in preprocessed[start:end] if char != '#'
        )
        
        return longest_palindromic_substring