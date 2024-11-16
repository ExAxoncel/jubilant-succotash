class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        order = []
        if numCourses <= 0:
            return order

        in_degree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        for pre in prerequisites:
            parent, child = pre[1], pre[0]
            graph[parent].append(child)
            in_degree[child] += 1

        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()
            order.append(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        if len(order) != numCourses:
            return []

        return order
