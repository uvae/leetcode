# 배열에서 양 끝에 가장 큰 값이 들어가고, 중간에 가장 작은 값이 들어가는 구간을 찾기
# 아이디어 0 : 단순 3중 loop로 돌기(최대 [100]*[99]*[98]번 루프)
# 아이디어 1 : O(N)에서 해결을 위해 DP의 접근법을 사용
# - 왼쪽부터 i번째까지 중 최대값을 계속 업데이트
# - 오른쪽도 동일하게 i번 선택에 대해서 이후 값들 중 가장 큰 값이 어떤건지
# - 최종적으로 루프를 다시 돌며, 해당 중간값에 대해 left_max[i-1]과 right_max[i+1]를 비교
#   어떤 값이 최대한의 효율이 되는지를 체크

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0; n = len(nums)
        l_max = [nums[0]] * n
        r_max = [nums[-1]] * n
        # 왼쪽, 오른쪽의 최대값을 미리 저장
        for i in range(1,n-2): l_max[i] = max(l_max[i-1], nums[i])
        for i in range(n-2,1,-1): r_max[i] = max(r_max[i+1], nums[i])
        # 중간값 기준으로 왼쪽 오른쪽을 비교하며 최대값 찾아감
        for i in range(1,n-1):
            val = (l_max[i-1] - nums[i]) * r_max[i+1]
            if(val > res): res = val

        return res
