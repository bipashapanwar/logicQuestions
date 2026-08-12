class Solution(object):
    def finalValueAfterOperations(self, operations):
        x=0
        for i in operations:
            if i in ('X++','++X'):
                x+=1
            elif i in ('X--','--X'):
                x-=1
        return x
            
        