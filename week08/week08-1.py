#題目給數字n ， return true 或 return false
#如果它是 2的很多次方 True ex:1,2,4,8,16....
#不是的話False ex: n%2 餘數不是0 就失敗

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n<=0:        #遇到0或負的都失敗
            return False

        while n>1:
            if n%2 != 0: #餘數不足就失敗
                return False
            else:
                n = n // 2 #要變小

        return True