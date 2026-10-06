class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(openB,closeB,stack):
            if openB == closeB == n:
                res.append("".join(stack.copy()))
                return
            
            if openB<n:
                stack.append("(")
                dfs(openB+1,closeB,stack)
                stack.pop()
            
            if closeB<openB:
                stack.append(")")
                dfs(openB,closeB+1,stack)
                stack.pop()
            
        dfs(0,0,[])
        return res
            


        
        
        