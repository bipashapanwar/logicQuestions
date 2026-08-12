class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        maxCandies=max(candies)
        for i in candies:
            if i+extraCandies>=maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result
        