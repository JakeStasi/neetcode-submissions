class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, number in enumerate(nums):

            comp = target - number

            if comp in seen:
                return [seen[comp], index]
            
            seen[number] = index
            

            
        