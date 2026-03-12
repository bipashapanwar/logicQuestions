class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count={} #empty dictionary to store count for each letter
        if len(ransomNote)>len(magazine):
            return False

        for ch in magazine:
            count[ch]=count.get(ch,0)+1
        
        for ch in ransomNote:
            count[ch]=count.get(ch,0)-1
            #check each immediately instead of another loop
            if count[ch]<0:
                return False
        return True
        
        return True
        