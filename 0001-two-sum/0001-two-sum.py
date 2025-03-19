'''
재귀방식으로 풀이 가능 : 하나를 선택해서 타겟값에서 제거하고, 나머지 배열에 대해 하나씩 줄여가며 가능한 방법을 탐색
2개의 합만 선택 가능하기에, 여기선 깊이를 더 들어갈 필요는 없음

[해시맵 방식 풀이]
- 2개의 합에서만 풀이를 하기에, N루프를 돌면서, 만약 필요한 값이 있다면 그 인덱스와 같이 반환하는 방법으로 구현
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # {값: 인덱스}

        for i, num in enumerate(nums):
            complement = target - num  # 필요한 값
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i  # 현재 숫자를 맵에 저장

        return []  # 문제에서 항상 해답이 존재한다고 가정됨
