import math
class Solution:
    def becomeFleet(self,k1_start_point,k1_hop_distance,k2_start_point,k2_hop_distance):
        if((k1_start_point > k2_start_point and k1_hop_distance > k2_hop_distance) or 
(k2_start_point > k1_start_point and k2_hop_distance > k1_hop_distance)):
            return -1
        multipler = k1_hop_distance-k2_hop_distance
        if(multipler == 0):
            return -1
        n = ((k2_start_point-k1_start_point)/multipler)+1
        if(n <= 0):
            return -1
        else:
            return (n-1)*k1_hop_distance+k1_start_point
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        fleet = len(position)
        combined.sort(key=lambda x:x[0])
        position[:], speed[:] = zip(*combined)
        cur_pos,cur_speed = position.pop(),speed.pop()
        while len(position) > 0:
            check_pos,check_speed = position.pop(),speed.pop()
            a = self.becomeFleet(cur_pos,cur_speed,check_pos,check_speed)
            if(a != -1 and a <= target):
                fleet -= 1
            else:
                cur_pos,cur_speed = check_pos,check_speed
        return fleet
