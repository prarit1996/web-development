class Solution:
    def fill(self, n, m, mat):
        for i in range(n):
            for j in range(m):
                if mat[i][j]=="O":
                    mat[i][j]="_"
        dir=[[0,-1],[-1,0],[0,1],[1,0]]
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m:
                return False
            if i==0 or j==0:
                if mat[i][j]=="X":
                    return True
                return False
            if mat[i][j]=="X":
                return True
            if mat[i][j]=="O":
                return False
            r=mat[i][j]
            mat[i][j]=-1
            d=True
            for x,y in dir:
                if 0<=x+i<n and 0<=y+j<m and mat[x+i][y+j]==-1:
                    continue
                d=d and dfs(x+i,y+j)
            mat[i][j]=r
            return d
               
        for i in range(n):
            for j in range(m):
                if mat[i][j]=="_":
                    if dfs(i,j):
                        mat[i][j]="X"
                    else:
                        mat[i][j]="O"
        return mat

s=Solution()
mat=[['X','O','X','O','O','O','X','O'],
     ['X','O','X','O','X','X','O','X'],
     ['O','X','O','X','X','X','O','O'],
     ['X','O','X','X','X','X','O','X'],
     ['X','X','X','O','O','X','X','X']
     ]
print(s.fill(5,8,mat))
