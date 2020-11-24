class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        result = []
        
        current = 0

        for i in nums:
            current += i
            result.append(current)
            
        return result
