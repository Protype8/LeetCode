class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        
        i = j = 0
        res = [matrix[i][j]]
        visited = set([(i,j)])
        cur_dir_index = 0
        changed_dir = False
        while True:
            di,dj = dirs[cur_dir_index%4]
            if(not i+di in range(len(matrix)) or not j+dj in range(len(matrix[0])) or (i+di,j
+dj) in visited):
                if(changed_dir):
                    break
                else:
                    cur_dir_index += 1
                    changed_dir = True
                    continue
            i += di
            j += dj
            visited.add((i,j))
            changed_dir = False
            res.append(matrix[i][j])
        return res
