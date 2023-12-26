#"00111" 想知道左邊幾個0，右邊幾個1 加起來最多
# for left in range(1,N-1) 0...left左邊 右邊left+1...N-1
class Solution:
    def maxScore(self, s: str) -> int:
        N=len(s)
        ans = 0
        for left in range(1,N-1):
            #接下來測左邊幾個0，右邊幾個1
            now = 0      #現在測試值多少
            for i in range(N): #每個字母都檢查
                if i<=left and s[i]=='0':now += 1 #左邊的0
                if i>left and s[i]=='1':now += 1  #右邊的1
            if now>ans: ans = now  #迴圈中間更新答案
        return ans
