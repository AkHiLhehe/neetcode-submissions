class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(0,len(nums)):
            # dupicate values avoider
            if i > 0 and nums[i]==nums[i-1]:  
                continue  #chekcind duplicate values for positive i and prev and current element
            left= i+1
            right= len(nums)-1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if total > 0:
                    right-=1
                elif total < 0:
                    left+=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left-1]:
                        left+=1
        return res
