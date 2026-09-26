import heapq

class Solution:
    def shortestPath(self, n, edges, src):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [float('inf')] * n
        dist[src] = 0

        pq = [(0, src)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = d + w

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        result = {}

        for i in range(n):
            if dist[i] == float('inf'):
                result[i] = -1
            else:
                result[i] = dist[i]

        return result
