# encoding: utf-8
from dfs_client import *
import mincemeat

#��� ������������ ������������������ ����� ������������ �� F1 + F2 �����
#��� F1 - ���-�� ������ ������ �������, F2 - ������
#��������� ��������� ������������ � ���� result.dat ���������

# ������ ��������� (file, file)
# ������ ���� (key, value), ��� key = (i, j) ���� �����,
# ��������������� ������ �������������� �������
# value = (matrix_num, k, value)
# ��� k - �����, ����������� ������� �������� ������� ����� �����������
def mapfn(k, v):
    left_matrix_num = 1     #��������� ��� ������� ������
    right_matrix_num = 2
    matrix_num = None       #����� ������� �������
    start = None            #������ ����� � ������� �����
    end = None              #����� ����� � ������� �����
    m = 3       #��������� ��� ������������ ������
    k = 4       # m x k, k x n
    n = 6
    for l in get_file_content(v):
        if matrix_num is None:
            matrix_num, start, end = l.split(" ", 2)
            matrix_num = int(matrix_num)
            start = int(start)
            end = int(end)
            curr_i = start #���������� ��������������� �������� �������
            curr_j = 1
            continue
        values = [int(v) for v in l.split(" ")]
        if matrix_num == left_matrix_num:
            for elem_ij in values:
                for j in range(1, n + 1):
                    yield (curr_i, j), (matrix_num, curr_j, elem_ij)
                curr_j += 1
            if curr_j > k:          #��� �������� ������ � �������
                curr_i += 1
                curr_j = 1
        else:
            for elem_ij in values:
                for i in range(1, m + 1):
                    yield (i, curr_j), (matrix_num, curr_i, elem_ij)
                curr_j += 1
            if curr_j > n:
                curr_i += 1
                curr_j = 1
    if curr_i != end + 1 or curr_j != 1:   #�������� �������� ����������� ������
        raise Exception("Bad size of matrix number = {}".format(matrix_num))


# �������� ��������� ������� (i, j) �������������� ������� � ������ k = (i,j)
def reducefn(k, vs):
    left_matrix_num = 1     #��������� ��� ������� ������
    right_matrix_num = 2
    (i, j) = k
    #��������� �� ��� ������ (�������� ����� ������� � ������)
    list1 = [(v[1], v[2]) for v in vs if v[0] == left_matrix_num] 
    list2 = [(a,b) for (matrix_num, a, b) in vs if matrix_num == right_matrix_num]
    list1.sort() #��������� ��� ��������� ������������
    list2.sort()
    result = sum([v[0][1] * v[1][1] for v in zip(list1, list2)])
    return result

s = mincemeat.Server()

# ������ ������ ������, �� ������� ������� �������
matrix_files = [l for l in get_file_content("/matrix1")]
for l in get_file_content("/matrix2"):
    matrix_files.append(l)
    
# � ������ ���� ������ �� ���� ��������
s.map_input = mincemeat.MapInputDFSFileName(matrix_files) 
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="") 

out_put_f = open('result.dat', 'w')
j = 1     # ������� ������ �������������� �������
for key, value in sorted(results.items()):
    if key[0] != j:       #���� ������� �� ����� ������
        out_put_f.write('\n')
        j = key[0]
    out_put_f.write("{} ".format(value))
out_put_f.close()