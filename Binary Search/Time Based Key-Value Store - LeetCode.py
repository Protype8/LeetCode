class TimeMap:

    def __init__(self):
        self.timestamp_dict = {}
        self.real_dict = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key in self.timestamp_dict):
            self.timestamp_dict[key].append(timestamp)
        else:
            self.timestamp_dict[key] = [timestamp]
        self.real_dict[(key,timestamp)] = value
    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.timestamp_dict):
            return ""
        cloest_time = self.binary_search(timestamp,self.timestamp_dict[key])
        if(cloest_time > timestamp):
            return ""
        else:
            return self.real_dict[(key,cloest_time)]
    def binary_search(self,target,nums):
        start , end = 0 ,len(nums) - 1 
        while start  <=  end:
            mid = (start + end ) // 2
            if(nums[mid] == target):
                return nums[mid]
            elif nums[mid] > target:
                end = mid - 1 
            else:
                start = mid + 1
        return nums[end]
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
