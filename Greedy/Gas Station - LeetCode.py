class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas) < sum(cost)):
            return -1
        i = 0
        while i < len(gas):
            current_tank = gas[i]
            current_index = 0
            while current_index < len(gas):
                new_pos = (i+current_index)%len(gas)
                if(current_tank < cost[new_pos]):
                    break
                current_tank -= cost[new_pos]
                current_index+=1
                new_pos = (i+current_index)%len(gas)
                current_tank += gas[new_pos]
            else:
                if(current_tank >= cost[new_pos]):
                    return i
            i = new_pos if new_pos > i else i+1
        return -1
