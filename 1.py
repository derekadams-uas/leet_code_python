class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if (value1 + value2) == target and index1 != index2:
                    return [index1, index2]
