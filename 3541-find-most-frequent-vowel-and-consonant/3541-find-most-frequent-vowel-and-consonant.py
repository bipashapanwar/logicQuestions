class Solution(object):
    def maxFreqSum(self, s):
        count,highestVowel,highestConsonant={},0,0
        for i in s:
            count[i]=count.get(i,0)+1
        for i in count:
            if i in ('a','e','i','o','u') and count[i]>highestVowel:
                highestVowel=count[i]
            elif not i in ('a','e','i','o','u') and count[i]>highestConsonant:
                highestConsonant=count[i]
        return highestVowel+highestConsonant

        

        