class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=  len(t):  #檢查兩個字串長度
            return False       #若長度不同就錯了

        d = {}  #空字典
        for c in s:
            if c in d:
                d[c] = d[c]+1
            else:
                d[c] = 1
        #print(d)
        for c in t:
            if c not in d:    #不再統計的字典內
                return False
            if d[c] <= 0:     #不夠
                return False
            else:
                d[c] =d[c] - 1
        
        return True