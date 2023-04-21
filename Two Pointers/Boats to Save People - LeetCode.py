class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        count = 0
        current_weight = 0
        boats = 0
        right = len(people)-1
        while right >= left:
            if(current_weight+people[right] <= limit):
                current_weight += people[right]
                count += 1
                right -= 1
            elif(current_weight+people[left] <= limit):
                current_weight += people[left]
                count += 1
                left += 1
            else:
                current_weight = 0
                count = 0
                boats+=1
            if(current_weight == limit or left > right or count == 2):
                current_weight = 0
                count= 0
                boats+=1
        return boats

