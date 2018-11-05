import numpy as np
flag=True
row=0
column=0
row_str=""
col_str=""
f=open("/home/talha/Documents/sequences.txt")
for W in f:
    if flag==True:
        row=len(W)
        row_str=W
    else:
        column=len(W)
        col_str=W
    flag=False
f.close()
matrix=np.zeros((row,column),np.int32)

#scoring
mismatch=input("enter mismatch score")
indel=input("enter indel score")
match=input("enter match score")


def _compute_array():
    for i in range(1, row):
        for j in range(1, column):
            matrix[i,j] = max(  matrix[i-1, j-1] + _get_score(i, j),
                                    matrix[i-1, j] + indel,
                                    matrix[i, j-1] + indel)
def _get_score( i, j):
    if row_str[i-1]==col_str[j-1]:
        return match
    else:
        return mismatch 
def _get_aligned_pair( i, j):
    if i>0:
        n1=row_str[i-1]
    else:
        n1='_'
    if j>0:
        n2=col_str[j-1]
    else:
        n2='_'
    return (n1, n2)

def _traceback():
    alignment= []
    i = row-1
    j = column-1
    while i >0 and j>0:
        if matrix[i-1, j-1] + _get_score(i, j) == matrix[i,j]:
            alignment.append((row_str[i-1],col_str[j-1]))
            i -= 1
            j -= 1
        elif matrix[i-1, j] + indel == matrix[i,j]:
            alignment.append(_get_aligned_pair(i, 0))
            i -= 1
        else:
            alignment.append(_get_aligned_pair(0, j))
            j -= 1
    alignment.reverse()
    print alignment  
flag=True
matrix[0,0]=0
matrix[0,1]=indel 
matrix[1,0]=indel
for i in range(0,1):
    for j in range(2,column):
        matrix[i][j]=matrix[i][j-1]+indel
for i in range(0,1):
    for j in range(2,row):
        matrix[j][i]=matrix[j-1][i]+indel
_compute_array()
_traceback()
print matrix
