lass Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:                #負的數一定錯，0也是錯的
            return False

        while n>1 :
            if n % 2 != 0:      #有餘數，失敗
                return False    #失敗
            else:
                n = n//2            #16//2得8，數字變小

        return True
        