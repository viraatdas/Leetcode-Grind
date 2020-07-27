class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        adj_list = [[] for _ in range(n)]

        for i, mem in enumerate(manager):
            if mem != -1:
                adj_list[mem].append(i)
        
        def dfs(i):
            time = 0
            for child in adj_list[i]:
                time = max(time, dfs(child))
            return time + informTime[i]
            
        return dfs(headID)
         
