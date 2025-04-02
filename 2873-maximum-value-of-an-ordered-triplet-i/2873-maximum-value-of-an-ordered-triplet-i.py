# 배열에서 양 끝에 가장 큰 값이 들어가고, 중간에 가장 작은 값이 들어가는 구간을 찾기
# 아이디어 0 : 단순 3중 loop로 돌기(최대 [100]*[99]*[98]번 루프)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m = 0
        l = len(nums)
        for i in range(l-2):
            for j in range(i+1, l-1):
                for k in range(j+1, l):
                    v = (nums[i] - nums[j]) * nums[k]
                    if(v > m): m = v
    
        return m
