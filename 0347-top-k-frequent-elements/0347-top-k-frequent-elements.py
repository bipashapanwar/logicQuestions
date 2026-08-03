class Solution(object):
    def topKFrequent(self, nums, k):
        count={}
        solution=[]
        for ch in nums:
            count[ch]=count.get(ch,0)+1
        sortedCount=(sorted(count.items(),key=lambda item:item[1],reverse=True))
        for ch,freq in sortedCount[:k]:
            solution.append(ch)
        return solution

        