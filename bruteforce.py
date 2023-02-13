class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                r += 1
            elif nums[l] < nums[r]:
                nums[l + 1] = nums[r]
                l += 1
            print(nums)
        return l + 1

        
            

