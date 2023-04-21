class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [i+1 for i in range(len(edges))]
        def get_parent(index,depth=0):
            if(p[index-1] != index):
                return get_parent(p[index-1],depth+1)
            return index,depth+1
        ans = None
        for edge in edges:
            index1,depth1 = get_parent(edge[1])
            index2,depth2 = get_parent(edge[0])
            if(index1 == index2):
                ans = edge
            else:
                if(depth1 > depth2):    
                    p[index2-1] = index1
                else:
                    p[index1-1] = index2
  
        return ans
