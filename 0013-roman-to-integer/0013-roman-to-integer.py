# class Solution:
#     def romanToInt(self, s: str) -> int:
#         def matchRoman(c: str) -> int:
#             c_arr = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
#             v_arr = [1, 5, 10, 50, 100, 500, 1000]
#             index = c_arr.index(c)
#             return v_arr[index] # index
        
#         arr = [matchRoman(s[0])]
#         for i in range(1, len(s)):
#             c = matchRoman(s[i])
#             if(arr[i-1] < c): arr.append(c + arr[i-1] * -2)
#             else: arr.append(c)

#         return sum(arr)

# 최적화 : 반복 연산을 줄이고, 변수의 메모리 사용량을 줄임
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0  # 이전 숫자 저장

        for c in reversed(s):  # 오른쪽에서 왼쪽으로 처리 (연산 최소화)
            curr = roman_map[c]
            if curr < prev: total -= curr  # 작은 값이 앞에 있으면 뺌
            else: total += curr  # 그렇지 않으면 더함
            prev = curr  # 이전 값 업데이트

        return total