class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count a number of num
        nCount = {}
        for n in nums:
            if n in nCount:
                nCount[n] += 1
            else:
                nCount[n] = 1
        
        # 2. Sort by count
        sortedN = sorted(nCount.items(), key=lambda x:x[1], reverse=True)

        # 3. Return the 'k' most frequent elements
        return list(map(lambda x:x[0],sortedN[:k]))
        