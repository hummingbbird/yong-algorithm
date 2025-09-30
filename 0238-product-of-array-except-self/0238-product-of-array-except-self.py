from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans[i] = nums[i]를 제외한 values의 곱
        # 조건: 시간복잡도 O(n) / 나누기 연산 x
        # 중첩 for 문 안 된다는 뜻 !! -> 그럼 for문 1단으로 어떻게 해결할 수 있을까?
        ans = []
        
        n = 1
        for i in range(len(nums)):
            ans.append(n)
            n *= nums[i]
        
        n=1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= n
            n *= nums[i]
        return ans
