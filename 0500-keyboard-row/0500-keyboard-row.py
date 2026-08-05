class Solution(object):
    def findWords(self, words):
        solution=list()
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")
        for word in words:
            flag=True
            if word[0].lower() in row1:
                for ch in word.lower():
                    if not ch in row1:
                        flag=False  
                        break          
            if word[0].lower() in row2:
                for ch in word.lower():
                    if not ch in row2:
                        flag=False
                        break
            if word[0].lower() in row3:
                for ch in word.lower():
                    if not ch in row3:
                        flag=False
                        break
            if flag:
               solution.append(word)
        return solution

                

        