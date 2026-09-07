class TimeMap:

    def __init__(self):
        self.timemp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        mylist = self.timemp[key]
        ans = ''
        left = 0
        right = len(mylist) - 1

        while left <= right:
            mid = (left + right) // 2
            val = mylist[mid]

            if val[0] <= timestamp:
                ans = val[1]
                left = mid + 1
            else:
                right = mid - 1

        return ans
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)