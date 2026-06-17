#Solution 1 - Sorting approach
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        
# Time complexity: O(n log n) due to sorting
# Space complexity: O(n) due to the space used by the sorted lists

# Solution 2 - Hash map approach
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #check for length first.
            return False 

        count = {}

        for char in s:
            count[char] = count.get(char,0)+1 #count frequency.
        
        for char in t:
            if char not in count: #check if it exist in t
                return False
            
            count[char] -= 1 #decrease the count for each character in t.

            if count[char] < 0 : #check if any character count goes negative, which means t has more of that character than s.
                return False
        
        return True
    
# Time complexity: O(n) where n is the length of the strings, since we traverse both strings once.
# Space complexity: O(1) 
#we only count[char] < 0, because we already check the length, and if we have aab, and bba, either a will give -1, or b will give -1, so we only need to check if any character count goes negative. 

