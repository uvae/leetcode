'''
문제 해결을 위한 아이디어
- 우선 t,s 값이 크기에 두 반복을 하게 되면 메모리와 시간에서 큰 낭비가 발생하게 됨
- 그렇다면 s의 각 아이템에 대해 반복에 따른 최종 길이만을 알 수 있음 되지 않을까?
- 그러면 dp로 시작하는 알파벳, 그리고 반복 횟수를 더했을 떄 최종 길이를 기억하자

첫번 째 실패 : z에서 한 번 더 반복해야 길이가 2가 됨
두번 째 실패 : jqktcurgdvlibczdsvnsg, 7517에서 시간 초과가 발생
- dp와 tmp의 계산을 위해 무한히 계산되는 리소스가 큼
- 그렇기에 t는 고정되어 있으니까 tmp없이 DP만을 업데이트 하자
'''

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        dp = [1] * 26
        MOD = 10**9 + 7

        for _ in range(t):
            new_dp = [0] * 26
            for i in range(26):
                if i < 25:
                    new_dp[i] = dp[i + 1]
                else:
                    new_dp[i] = dp[0] + dp[1] % MOD
            dp = new_dp
        
        return sum(dp[ord(c) - 97] for c in s) % MOD
