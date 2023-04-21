class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List
[List[int]]) -> List[bool]:
        needed_courses = {i:[] for i in range(numCourses)}
        for p,q in prerequisites:
            needed_courses[p].append(q)
        print(needed_courses)
        visited = set()
        def dfs(index,looking):
            visited.add(index)
            if(index == looking):
                return True
            for pre in needed_courses[index]:
                if(pre not in visited and dfs(pre,looking)):
                    return True
            return False
        ans = []
        for query in queries:
            visited = set()
            ans.append(dfs(query[0],query[1]))
        return ans
        
