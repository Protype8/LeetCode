class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir_change = (1,0)
        pos_change = (0,0)
        for instruction in instructions:
            if(instruction == "L"):
                dir_change = (dir_change[1],dir_change[0]*-1)
            elif(instruction == "R"):
                dir_change = (dir_change[1]*-1,dir_change[0])
            else:
                pos_change = (pos_change[0]+dir_change[0],pos_change[1]+dir_change[1])
        if(pos_change == (0,0) or dir_change != (1,0)):
            return True
