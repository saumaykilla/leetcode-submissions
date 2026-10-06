class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs,preReq in prerequisites:
            preMap[crs].append(preReq)
        
        visit=set()

        def dfs(current):
            if current in visit:
                return False
            if preMap[current]==[]:
                return True
            visit.add(current)
            for preReq in preMap[current]:
                if not dfs(preReq):
                    return False
            visit.remove(current)
            preMap[current]=[]
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True