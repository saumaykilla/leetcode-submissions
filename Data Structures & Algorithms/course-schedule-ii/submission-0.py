class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {i: [] for i in range(numCourses)}

        for crs,preReq in prerequisites:
            preMap[crs].append(preReq)

        visit,cycle = set(),set()
        output=[]
        def dfs(current):
            if current in cycle:
                return False
            if current in visit:
                return True
            
            cycle.add(current)
            
            for course in preMap[current]:
                if not dfs(course):
                    return False
            cycle.remove(current)
            visit.add(current)
            output.append(current)
            return True
        
        for x in range(numCourses):
            if not dfs(x):
                return []
        return output