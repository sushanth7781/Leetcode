
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        vis={}
        def dfs(curr):
            if curr in vis:
                return vis[curr]
            copy=Node(curr.val)
            vis[curr]=copy
            for i in curr.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        return dfs(node)
    
        