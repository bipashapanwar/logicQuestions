class Solution(object):
    def detectCapitalUse(self, word):
        return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())