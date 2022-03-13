import codecs

txt_in = open("yq_in.txt", "r")
txt_read = txt_in.read()
txt_in.close()

txt = codecs.open('yq_in.txt', 'r')
line = txt.readline()   # 以行的形式进行读取文件
list1 = []
list2 = []
while line:
    a = line.split()
    b = a[1:3]  # 提出地区和数量的列
    list2.append(b)  # 将地区和数量添加在新列表中
    line = txt.readline()
txt.close()

txt_out = open("yq_out.txt", "w") # 把地区和数量暂存在yq_out.txt中
for i in list2:
    txt_out.writelines(i)
    txt_out.write('\n')
txt_out.close()

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []

with open("yq_out.txt", 'r', ) as t:
    line = t.readlines()

    for i1, rows in enumerate(line):
        if i1 in range(1, 12):
            data1.append(rows)

    for i2, rows in enumerate(line):
        if i2 in range(13, 24):
            data2.append(rows)

    for i3, rows in enumerate(line):
        if i3 in range(25, 45):
            data3.append(rows)

    for i4, rows in enumerate(line):
        if i4 in range(46, 58):
            data4.append(rows)

    for i5, rows in enumerate(line):
        if i5 in range(59, 72):
            data5.append(rows)

    for i6, rows in enumerate(line):
        if i6 in range(73, 88):
            data6.append(rows)

    for i7, rows in enumerate(line):
        if i7 in range(89, 101):
            data7.append(rows)

    for i8, rows in enumerate(line):
        if i8 in range(102, 120):
            data8.append(rows)

    for i8, rows in enumerate(line):
        if i8 in range(121, 129):
            data8.append(rows)

    for i9, rows in enumerate(line):
        if i9 in range(121, 129):
            data9.append(rows)

t.close()
# #写入
with open("yq_out.txt", "w", ) as f:
    f.write('浙江省\n')
    for i1 in range(len(data1)):
        f.writelines(data1[i1])
    f.write('\n江西省\n')
    for i2 in range(len(data2)):
        f.writelines(data2[i2])
    f.write('\n广东省\n')
    for i3 in range(len(data3)):
        f.writelines(data3[i3])
    f.write('\n江苏省\n')
    for i4 in range(len(data4)):
        f.writelines(data4[i4])
    f.write('\n湖南省\n')
    for i5 in range(len(data5)):
        f.writelines(data5[i5])
    f.write('\n安徽省\n')
    for i6 in range(len(data6)):
        f.writelines(data6[i6])
    f.write('\n陕西省\n')
    for i7 in range(len(data7)):
        f.writelines(data7[i7])
    f.write('\n河南省\n')
    for i8 in range(len(data8)):
        f.writelines(data8[i8])
    f.write('\n贵州省\n')
    for i9 in range(len(data9)):
        f.writelines(data9[i9])
print('输出到yq_out.txt完成')
f.close()