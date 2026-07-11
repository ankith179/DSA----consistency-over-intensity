from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        complete_components_count = 0
        
        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)
                
                v_count = len(component)
                is_complete = True
                
                for node in component:
                    if len(adj[node]) != v_count - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components_count += 1
                    
        return complete_components_count