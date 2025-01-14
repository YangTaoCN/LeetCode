#bfs each number and each char and each str in res ,append level by level
#dfs from the first number ,use recursive and track back ,plus then next char and minus back


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #bfs
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz"}
        # result = [""]
        # for digit in digits:
        #     lst = dic[digit]
        #     newresult = []
        #     for char in lst:
        #         for str in result:
        #             newresult.append(str+char)
        #     result = newresult
        # return result
        
        #dfs
        res = []
        if not digits:
            return res
        self.dfs(digits,0,'',dic,res)
        return res
        
    def dfs(self,digits,i,cur,dic,res):
        if i == len(digits):
            res.append(cur)
            return 
        for ch in dic[digits[i]]:
            cur = cur + ch
            self.dfs(digits,i+1,cur,dic,res)
            cur = cur[:-1]
            
    
    
    
    
    
    
    
    
    
    
    
    
    
