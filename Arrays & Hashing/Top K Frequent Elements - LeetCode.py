class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_list = {}
        for num in set(nums):
            if(nums.count(num) in number_list):
                number_list[nums.count(num)].append(num)
            else:
                number_list[nums.count(num)] = [num]
        print(number_list)
        sorted_list = sorted(number_list.keys(),reverse=True)
        print(sorted_list)
        output_list= []
        i = 0
        counter = 0
        while counter < k:
            num = number_list[sorted_list[i]].pop()
            if(number_list[sorted_list[i]] == []):
                i += 1
            output_list.append(num)
            counter += 1
        return output_list
