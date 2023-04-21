class Solution:
    def trap(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = 0
        trapped_water = 0
        max_left_list = [0]
        max_right_list = [0]
        current_left_max = 0
        current_right_max = 0
        for i in range(1,len(height)):
            if(height[i-1] > current_left_max):
                current_left_max = height[i-1] 
            max_left_list.append(current_left_max)
        for i in range(1,len(height)):
            if(height[len(height)-i] > current_right_max):
                current_right_max = height[len(height)-i] 
            max_right_list.append(current_right_max)
        max_right_list = max_right_list[::-1]
        for i in range(0,len(height)):
            trapped_water += max(0,min(max_right_list[i],max_left_list[i])-height[i])
        return trapped_water
