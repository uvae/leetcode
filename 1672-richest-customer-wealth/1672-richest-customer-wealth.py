class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = 0
        for arr in accounts:
            acc_sum = sum(arr)
            if(acc_sum > m): m = acc_sum
        
        return m
