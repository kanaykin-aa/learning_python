class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map={}
        for i, n in enumerate(nums):
            dif=target-n
            if dif in hash_map:
                return [hash_map[dif], i]
            else:
                hash_map[n]=i