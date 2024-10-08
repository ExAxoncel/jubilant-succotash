class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin = 0
        end = len(numbers) - 1
        res = []
        
        while begin < end:
            if numbers[begin] + numbers[end] == target:
                res.append(begin + 1)
                res.append(end + 1)
                return res
            elif numbers[begin] + numbers[end] < target:
                begin += 1
            else:
                end -= 1
        
        return [0, 0]
