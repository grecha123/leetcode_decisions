class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unic_num = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[unic_num-1]:
                nums[unic_num] = nums[i]
                unic_num += 1 
        return unic_num