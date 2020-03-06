# !/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# import sys
# import imp
# imp.reload(sys)

import xlrd
import os
import io

#设置文件路径
bait_type_path = os.path.dirname(__file__)
fname1=xlrd.open_workbook(os.path.join(bait_type_path, "excelDate.xlsx"),'r')
fname2=io.open(os.path.join(bait_type_path, "condition.txt"),'r',encoding='utf-8')



# fname1=xlrd.open_workbook('C:\\Users\\zxc\Desktop\\filterExcel\\excelDate.xlsx','r')
# fname2=open('C:\\Users\\zxc\Desktop\\filterExcel\\condition.txt','r',encoding='utf-8')

# 获取当前文件的表格
sheets=fname1.nsheets
# print('sheets-----',sheets)

sheet2=fname1.sheet_by_index(0)  #获取表对象
# print('sheet2---',sheet2)

#获取行数
nrows = sheet2.nrows
# 获取列数
ncols = sheet2.ncols
# 获取某一行的数据
sheet_rows=sheet2.row_values(1)
# 获取第一行 1-2列的数据
sheet_rowss=sheet2.row_values(1,1,3)
# 获取第1行第0列的数据
sheet_cells=sheet2.cell_value(1,0)
###除了cell值内容外还有附加属性，如：text:"字段名"
sheet_cell=sheet2.cell(1,0)
#获取第一列，第二行以下的数据
sheet_cols=sheet2.col_values(1,2)
# 获取第一列，第二至第四行的数据
sheet_cols1=sheet2.col_values(1,2,5)




# 获取各行的数据
sheet_rowslist=[]
for i in range(5,nrows):
    sheet_rowslist.append(sheet2.row_values(i,1))
    rows_list=sheet2.row_values(i,1)
    if ''.__eq__(str(rows_list[0])):
        print(i+1,'name is null')
    if ''.__eq__(str(rows_list[1])) or str(rows_list[1])==None or len(rows_list[1])!=64 :
        print(i+1,'pid is null or len less than 64')
    if ''.__eq__(str(rows_list[2])) or str(rows_list[2])==None or len(rows_list[2])!=64 :
        print(i+1,'mobile is null or len less than 64')

