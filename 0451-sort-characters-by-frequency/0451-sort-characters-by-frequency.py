class Solution(object):
    def frequencySort(self, s):
        count={}
        solution=''
        for ch in s:
            count[ch]=count.get(ch,0)+1
        sortedCount=sorted(count.items(), key=lambda item:item[1],reverse=True)
        for ch,freq in sortedCount:
            solution+=ch*freq
        return solution