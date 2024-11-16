class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
