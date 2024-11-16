class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        
        queue = deque()
        flesh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    flesh += 1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        time = 0
        
        while queue:
            x, y, time = queue.popleft()
            time = max(time, time)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    flesh -= 1
                    queue.append((nx, ny, time + 1))
        
        if flesh == 0:
            return time
        else:
            return -1
