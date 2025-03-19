'''
binary array가 들어오고, 연결된 bit 3개를 flip(0 -> 1, 1 -> 0) 가능함
그럴 때 모든 비트들이 1로 될 수 있나? 된다면 몇 번이 걸리는지 / 안되면 -1
배열의 크기가 3 ~ 100,000까지 들어오기에 성능 제한이 걸림

[로직 구현]
단순하게는 0부터 ~ n-2 까지 돌며 자리수 전환이 필요한 경우 flip하며 구현이 가능함
마지막에는 3bit가 1이면 완성된 것 / 안되면 불가능

[성능 개선]
그러면 이제 로직이 개선 가능한 부분을 확인
- 반복문을 얼마나 줄일 수 있는지 : 내부 반복문을
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums) - 2):
            if(nums[i]): continue
            nums[i] ^= 1
            nums[i+1] ^= 1
            nums[i+2] ^= 1
            c +=1 

        return c if all(nums) else -1
