class Solution:
    def romanToInt(self, s: str) -> int:
        def matchRoman(c: str) -> int:
            c_arr = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
            v_arr = [1, 5, 10, 50, 100, 500, 1000]
            index = c_arr.index(c)
            return v_arr[index] # index
        
        arr = [matchRoman(s[0])]
        for i in range(1, len(s)):
            c = matchRoman(s[i])
            if(arr[i-1] < c): arr.append(c + arr[i-1] * -2)
            else: arr.append(c)

        return sum(arr)