class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = {} # i, num

        for i, num in enumerate(nums):
            need = target - num
            if need in hist:
                return [hist[need], i]
            hist[num] = i
        
        return False