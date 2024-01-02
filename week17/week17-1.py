class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()            #先排數字
        ans = [[nums[0]]]      #把最小數字，放在兩層括號裡
        repeat=0               #目前數字 nums沒重複
        N = len(nums)
        for i in range(1, N):  #有幾個數字
            if nums[i]==nums[i-1]:
                repeat += 1
                if len(ans)<=repeat:
                    ans.append([])
            else:
                repeat =0
            ans[repeat].append(nums[i])
        return ans