class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_side = deque(cardPoints[0:k])
        right_side = deque(cardPoints[len(cardPoints)-k:])
        left_sum = sum(left_side)
        right_sum = sum(right_side)
        s = 0
        while k:
            if(left_sum < right_sum):
                l,r = left_side.pop(),right_side.pop()
                s += r
            else:
                l,r = left_side.popleft(),right_side.popleft()
                s += l
            left_sum -= l
            right_sum -= r
            k-=1
        return s
