matrix=[]
for i in range(4):
    matrix.append([0]*4)
print(matrix)
rows=4
cols=4
moves=0
i=0
j=0
count=1
while (rows>0 and cols>0):
    while (moves<cols):
        matrix[i][j]=count
        count+=1
        moves+=1
        j+=1
    rows-=1
    i+=1
    j-=1
    print(matrix)
    moves=0
    while (moves<rows):
       matrix[i][j]=count
       count+=1
       moves+=1
       i+=1
    cols-=1
    i-=1
    j-=1
    moves=0
    while(moves<cols):
        matrix[i][j]=count
        count+=1
        j-=1
        moves+=1
    rows-=1
    i-=1
    j+=1
    print(matrix)
    moves=0
    while(moves<rows):
        matrix[i][j]=count
        count+=1
        i-=1
        moves+=1
    cols-=1
    i+=1
    j+=1
    print (matrix)
print(matrix)
    # moves=0
    # while(moves<cols):
    #     matrix[i][j]=count
    #     moves+=1
    #     j+=1
    #     count+=1
    # rows-=1
    # i+=1
    # j-=1
    # print (matrix)
    # while(moves<rows):
    #     matrix[i][j]=count
    #     count+=1
    #     j-=1
    #     moves+=1
    # rows-=1
    # i-=1
    # j+=1
    print(matrix)
    

    



    
      
    


    