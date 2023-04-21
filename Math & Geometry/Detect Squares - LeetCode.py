class DetectSquares:

    def __init__(self):
        self.point_dict = {}
    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.point_dict[point] = self.point_dict.get(point,0)+1
    def count(self, query_point: List[int]) -> int:
        res = 0
        for point in self.point_dict:
            if(point[0] == query_point[0] or point[1] == query_point[1]):
                continue
            if(abs(point[0]-query_point[0]) == abs(point[1]-query_point[1])):
                
                if((point[0],query_point[1]) in self.point_dict and (query_point[0],point[1]) in 
self.point_dict):
                    res += self.point_dict[(point[0],query_point[1])]*self.point_dict[
(query_point[0],point[1])]*self.point_dict[point]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
