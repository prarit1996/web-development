from collections import defaultdict
import heapq,math
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def add_edge(self,x,y):
        self.graph[x].append(y)
def dfs1(root,g,visited,st):
    visited[root]=True
    for x in g.graph[root]:
        if not visited[x]:
            dfs1(x,g,visited,st)
    st.append(root)
def dfs2(root,g,visited):
    print(root,end=" ")
    visited[root]=True
    for x in g.graph[root]:
        if not visited[x]:
            dfs2(x,g,visited)
def reversedGraph(g):
    g1=Graph(g.v)
    for x in g.graph:
        for y in g.graph[x]:
            g1.add_edge(y,x)
    return g1
def kosaraju(V,edges):
    g=Graph(V)
    for x,y in edges:
        g.add_edge(x,y)
    visited=[False]*V
    st=[]
    for i in range(V):
        if visited[i]==False:
            dfs1(i,g,visited,st)
    g1=reversedGraph(g)
    visited=[False]*V
    while st:
        root=st.pop()
        if not visited[root]:
            dfs2(root,g1,visited)
            print()

V=5
edges=[[1,0],[2,1],[0,2],[0,3],[3,4]]
kosaraju(V,edges)
    
    
    
    
