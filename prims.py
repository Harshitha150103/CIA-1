# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
adj_mat=[]
inf_val=9999
chk=0

print("the no.of rows and columns are the no.of vertices in your graph\n")
row_no=int(input("enter the no.of rows of the adjacency matrix : "));
column_no=int(input("enter the no.of columns of the adjacency matrix : "))

for i in range(row_no):
    arr=[]
    print("enter elements of row ",i)
    for j in range(column_no):
        arr.append(int(input()))
    adj_mat.append(arr)

root_node=[0]*row_no
print(root_node)
root_node[0]=True  

print(adj_mat)
for i in range(row_no):
    for j in range(column_no):
        print(adj_mat[i][j],end=" ")
    print("\n")

print("Edge","Weight",sep="     ")
while(chk < row_no-1):
    min_val=inf_val
    a=0
    b=0
    for k in range(row_no):
        if root_node[k]:
            for l in range(row_no):
                if((root_node[l]!=True) and adj_mat[k][l]):
                    if(min_val>adj_mat[k][l]):
                        min_val=adj_mat[k][l]
                        a=k
                        b=l
    print(a,"--->",b,"  ",adj_mat[a][b])
    root_node[b]=True
    chk+=1