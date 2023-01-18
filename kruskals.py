#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:54:02 2023

@author: iot-b1
"""

def find_min(i):
    while arr[i] != i:
        i = arr[i]
    return i

def union1(i, j):
    a = find_min(i)
    b = find_min(j)
    arr[a] = b

def kruskal(cost,row_no):
    mincost = 0 
    for i in range(row_no):
        arr[i] = i

    edge_ct = 0
    while edge_ct < row_no - 1:
        min = 9999
        a = -1
        b = -1
        for i in range(row_no):
            for j in range(row_no):
                if find_min(i) != find_min(j) and cost[i][j] < min:
                    min = cost[i][j]
                    a = i
                    b = j
        union1(a, b)
        print("edge",edge_ct,":","(",a,b,")","     ","cost : ",min)

        edge_ct += 1
        mincost += min
    print("\n")
    print("Minimum cost = ",mincost)
adj_mat=[]
print("the no.of rows and columns are the no.of vertices in your graph\n")
row_no=int(input("enter the no.of rows of the adjacency matrix : "));
column_no=int(input("enter the no.of columns of the adjacency matrix : "))

for i in range(row_no):
    arr1=[]
    print("enter elements of row ",i)
    for j in range(column_no):
        arr1.append(int(input()))
    adj_mat.append(arr1)
arr = [i for i in range(row_no)]
kruskal(adj_mat,row_no)