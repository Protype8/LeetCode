class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_taken = [math.ceil(dist[i]/speed[i]) for i in range(len(dist))]
        time_taken.sort()
        current = 0
        for time in time_taken:
            if(time <= current):
                print(time)
                break
            current += 1
        return current
