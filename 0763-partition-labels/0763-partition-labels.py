class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partition = []
        start, end = 0, 0
        
        last = {c: i for i, c in enumerate(s)}
        # last = [-1] * 26 # 딕셔너리 대신 어레이로 메모리 개선
        # for i in range(len(s)): last[ord(s[i]) - ord('a')] = i
        # for i in range(len(s)):
        for i, c in enumerate(s):
            # end = max(end, last[ord(s[i]) - ord('a')])
            end = max(end, last[c]) # 현재 루프 중 더 뒤에 끝나는 문자열이 있으면, 지점을 옮김
            if(i == end): # 만약 루프 중 더이상 뒷 지점에 있는거 없는 경우 (모든 문자열이 포함된게 뒤에선 더 이상 안나옴)
                partition.append(end - start + 1) # 시작점에서 얼마나 오면 되는지 알림
                start = i + 1
        
        return partition
