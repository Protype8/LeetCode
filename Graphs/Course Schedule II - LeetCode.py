class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        needed_courses = {i:[] for i in range(numCourses)}
        visited = set()
        current = set()
        path = []
        for p,q in prerequisites:
            needed_courses[p].append(q)
        def dfs(index):
            if(index in current):
                return False
            if(index in visited):
                return True
            visited.add(index)
            if(needed_courses[index] == []):
                path.append(index)
                return True
            current.add(index)
            for pre in needed_courses[index]:
                if(not dfs(pre)):
                    return False
            current.remove(index)
            path.append(index)
            return True
        for i in range(numCourses):
            if(i not in visited and not dfs(i)):
                return []
        return path
    
