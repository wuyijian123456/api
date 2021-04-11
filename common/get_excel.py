import xlrd

excel=xlrd.open_workbook(r"C:\Users\Administrator\Desktop\user.xls")
table=excel.sheets()[0]
print(table.nrows)#打印行数
print(table.ncols)#读取列数
print(table.row_values(0))#读取第一行的值
list=[]
for i in range(1,table.nrows):
    dict={}
    for j in range(table.ncols):
        dict[table.row_values(0)[j]] = table.row_values(i)[j]
    list.append(dict)
print(list)


print(tuple(list))










