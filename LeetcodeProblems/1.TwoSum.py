class Solution:
    def twoSum(self, nums, target):
        # Loop through each number in the list
        for i in range(len(nums)):
            # Check the remaining numbers
            for j in range(i + 1, len(nums)):
                
                # Check if nums[i] + nums[j] = target
                if nums[i] + nums[j] == target:
                    
                    # If yes, return their indices
                    return [i, j]

nums = [2, 7, 11, 15]  # example list
target = 9             # target value

obj = Solution()        # create object of class
result = obj.twoSum(nums, target)  # call function

print(result)           # print output