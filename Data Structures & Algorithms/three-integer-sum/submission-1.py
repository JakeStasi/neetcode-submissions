class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        
        ans = []

        

        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            
            

            right = len(nums) - 1
            left = x + 1
            while left < right:
                
                if nums[left] + nums[right] > -nums[x]:
                    right -= 1
                
                elif nums[left] + nums[right] < -nums[x]:
                    left += 1

                elif nums[left] + nums[right] == -nums[x]:
                    ans.append([nums[x],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left +1]:
                        left += 1
                    while right > left and nums[right] == nums[right -1]:
                        right -= 1
                    right -= 1
                    left += 1
                    
        return ans
                
                
            