grid=[[0,0,1,0,1],
      [0,1,0,0,1],
      [0,1,0,0,1],
      [0,0,1,0,1]]
for i in range(1,21):
    neighbours=[(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
    rows=len(grid)
    cols=len(grid[0])
    copy_grid=[[grid[row][col] for col in range(cols)]for row in range(rows)]
    for row in range(rows):
        for col in range(cols):
            live_neighbors=0
            for neighbour in neighbours:
                r=(row+neighbour[0])
                c=(col+neighbour[1])
                if((r<rows and r>=0) and (c<cols and c>=0) and (copy_grid[r][c]==1)):
                    live_neighbors+=1
            #rule 1
            if(copy_grid[row][col]==1 and live_neighbors<2):
                grid[row][col]=0
            #rule 2
            if(copy_grid[row][col]==1 and live_neighbors>3):
                grid[row][col]=0
            #rule 3
            if(copy_grid[row][col]==0 and live_neighbors==3):
                grid[row][col]=1
    print(grid)
