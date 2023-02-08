

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        startIndex = 0
        endIndex = len(nums)-1

        while (endIndex-startIndex>1):
            
            mid = (startIndex+endIndex)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                endIndex = mid 
            else:
                 startIndex = mid 
           
        if target<=nums[startIndex]:
            return startIndex
        elif target<=nums[endIndex]:
            return endIndex
        else:
            return endIndex+1
        
        

solve = Solution()
print(solve.searchInsert([1,3], 3))