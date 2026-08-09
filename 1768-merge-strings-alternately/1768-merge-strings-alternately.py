class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged=''
        n=min(len(word1),len(word2))
        for i in range(n):
            merged+=word1[i]
            merged+=word2[i]
        if len(word1)>len(word2):
            merged+=word1[n:]
        else:
            merged+=word2[n:]
        return merged
        