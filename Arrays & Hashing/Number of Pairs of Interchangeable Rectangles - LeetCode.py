class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        output = 0
        width_to_height_ratio = {}
        for rectangle in rectangles:
            ratio = rectangle[0]/rectangle[1]
            interchangeables = width_to_height_ratio.get(ratio,0)
            output+=interchangeables
            width_to_height_ratio[ratio] = interchangeables+1
        return output
