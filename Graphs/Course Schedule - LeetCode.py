class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        needed_courses = {i:[] for i in range(numCourses)}
        visited = set()
        current = set()
        for p,q in prerequisites:
            needed_courses[p].append(q)
        def dfs(index):
            if(index in current):
                return False
            if(index in visited):
                return True
            if(needed_courses[index] == []):
                return True
            current.add(index)
            visited.add(index)
            for pre in needed_courses[index]:
                if(not dfs(pre)):
                    return False
            current.remove(index)
            return True
        for i in range(numCourses):
            if(i not in visited and not dfs(i)):
                return False
        return True
    
