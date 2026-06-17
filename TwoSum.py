class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in seen:
                return [seen[compliment], i]
            seen[num] = i
        return []

# Standard approach to solve the Two Sum problem is to use a hash map (dictionary) to store the numbers we have seen so far and their corresponding indices. As we iterate through the list of numbers, we calculate the complement (the number needed to reach the target) and check if it exists in our hash map. If it does, we return the indices of the complement and the current number. If it doesn't, we add the current number and its index to the hash map. This approach allows us to find the solution in linear time, O(n), since we only need to traverse the list once. The space complexity is also O(n) in the worst case, if all numbers are unique and we end up storing all of them in the hash map.
# Time complexity: O(n)
# Space complexity: O(n)
# Brute force approach would be O(n^2) time complexity, as we would have to check every pair of numbers to see if they add up to the target, using two loops.