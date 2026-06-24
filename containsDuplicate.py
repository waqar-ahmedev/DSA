class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

#Set removes the duplicates, so if the length of the set is not equal to the length of the original list, it means there were duplicates in the list. This approach has a time complexity of O(n) and a space complexity of O(n) in the worst case, where n is the number of elements in the input list.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            seen.add(n)
        return len(seen) != len(nums)
