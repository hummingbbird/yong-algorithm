class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nDict = {}
        for i in range(len(nums)):
            n = nums[i]
            if (target-n) in nDict:
                return [i, nDict[target-n]]
            else:
                nDict[n] = i