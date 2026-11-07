class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = []  #(server, idx)
        busy = []  #(time, server, idx)
        res = []

        for i in range(len(servers)):
            heapq.heappush(free, (servers[i], i))
  
        i = 0
        time = 0
        while i < len(tasks): 
            #print("time:",time,"\nres:", res,"\nfree:",free, "\nbusy:",busy)
            
            while busy and busy[0][0] <= time:
                  #print(True)
                  t,j = heapq.heappop(busy)
                  heapq.heappush(free, (servers[j], j))

            if free and i < len(tasks):
                fs, idx = heapq.heappop(free)
                res.append(idx)
                heapq.heappush(busy, (time + tasks[i],idx))
                i += 1
                time = max(time, i)
            else:
                time = busy[0][0]
                
        return res
        
        #3, 2, 1 ==>  6, 5, 4, 1, 2, 3
        #t = 3-5, all server busy
        #t = 6, all server free 
        