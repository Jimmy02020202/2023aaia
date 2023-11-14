lass Solution:
    def average(self, salary: List[int]) -> float:
        #print(sum(salary))
        #有陷阱，城市還不對

        total = sum(salary) - max(salary) - min(salary)  #全部加總減最大最小值
        N = len(salary) - 2   #因扣掉最大最小值，數目減2
        return total / N
       
        #return (sum(salary) - max(salary) - min(salary)) / (len(salary) -2)