class Solution(object):
    def uniqueOccurrences(self, arr):
        count={}
        for i in arr:
            count[i]=count.get(i,0)+1
        uniqueFreq=set(count.values())
        if len(uniqueFreq)==len(count):
            return True
        return False
       
        
        