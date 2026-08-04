class Solution(object):
    import string
    def checkIfPangram(self, sentence):
        alpha=list(string.ascii_lowercase)
        for ch in alpha:
            if not ch in sentence:
                return False
        return True

        
        