def findCriticalPath(connections,n):
    s=set(connections)
    visited=[False for i in range(n)]
