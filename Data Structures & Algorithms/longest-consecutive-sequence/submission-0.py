class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        best = 0

        for num in numbers:
            if num - 1 in numbers:
                continue

            streak = 1
            while num + streak in numbers:
                streak += 1

            best = max(best, streak)
        return best